"""H2-only wire envelope; backend tools and H0 schemas stay unchanged."""
from copy import deepcopy

from .memory import validate_plan

MOTION_TOOLS = {'turn', 'move_relative', 'finish'}


class PlanEnvelopeError(ValueError):
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def validate_envelope(envelope):
    if not isinstance(envelope, dict):
        raise PlanEnvelopeError('PLAN_NOT_OBJECT')
    if set(envelope) not in ({'plan', 'subgoal_id'}, {'plan_id', 'subgoal_id'}):
        raise PlanEnvelopeError('PLAN_ENVELOPE_FIELDS')
    sid = envelope['subgoal_id']
    if not isinstance(sid, str) or not sid or len(sid) > 100:
        raise PlanEnvelopeError('INVALID_SUBGOAL_ID')
    if 'plan' in envelope:
        try:
            validate_plan(envelope['plan'])
        except (ValueError, TypeError, KeyError):
            raise PlanEnvelopeError('INVALID_PLAN_SCHEMA') from None
        if sid not in {g['subgoal_id'] for g in envelope['plan']['subgoals']}:
            raise PlanEnvelopeError('UNKNOWN_SUBGOAL_ID')
    elif not isinstance(envelope['plan_id'], str) or not envelope['plan_id'] or len(envelope['plan_id']) > 100:
        raise PlanEnvelopeError('INVALID_PLAN_ID')
    return envelope


def planning_tools(tools):
    tools = deepcopy(tools)
    condition = {'type': 'object', 'properties': {
        'object_id': {'type': 'string'}, 'measurement': {'type': 'string'},
        'op': {'type': 'string', 'enum': ['ge', 'le', 'eq']}, 'value': {'type': 'number'}},
        'additionalProperties': False,
        'description': 'Either object_id only, or measurement/op/value only.'}
    goal = {'type': 'object', 'properties': {
        'subgoal_id': {'type': 'string', 'maxLength': 100}, 'description': {'type': 'string'},
        'preconditions': {'type': 'array', 'items': condition, 'maxItems': 32},
        'completion': {'type': 'array', 'items': condition, 'maxItems': 32}},
        'required': ['subgoal_id', 'description', 'preconditions', 'completion'], 'additionalProperties': False}
    plan = {'type': 'object', 'properties': {
        'subgoals': {'type': 'array', 'items': goal, 'minItems': 1, 'maxItems': 32},
        'branches': {'type': 'array', 'items': {'type': 'object', 'properties': {
            'on': {'type': 'string'}, 'subgoal_id': {'type': 'string'}},
            'required': ['on', 'subgoal_id'], 'additionalProperties': False}},
        'recovery': {'type': 'string'}},
        'required': ['subgoals', 'branches', 'recovery'], 'additionalProperties': False}
    envelope = {'type': 'object', 'properties': {
        'plan': plan, 'plan_id': {'type': 'string'}, 'subgoal_id': {'type': 'string'}},
        'required': ['subgoal_id'], 'additionalProperties': False,
        'description': 'Required planning binding. Supply exactly plan+subgoal_id for a new plan, '
                       'or plan_id+subgoal_id to continue the current accepted plan. Never supply both.'}
    for tool in tools:
        if tool['function']['name'] in MOTION_TOOLS:
            schema = tool['function']['parameters']
            schema['properties']['planning'] = deepcopy(envelope)
            schema['required'] = [*schema.get('required', []), 'planning']
    return tools
