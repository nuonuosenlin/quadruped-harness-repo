"""Persistent workflow state and legal tool contracts. No simulation or network."""
import copy
from geometry import TOOLS


class Progress:
    def __init__(self):
        self.phase = 'track'
        self.executions = 0
        self.traj = None
        self.no_progress = 0
        self.error_counts = {}
        self.last_error = None

    @property
    def relation(self):
        return 'touch' if self.executions == 0 else 'adjust'

    def tools(self):
        names = {'track': {'track_keypoint', 'check_success'},
                 'plan': {'solve_constraint', 'track_keypoint', 'check_success'},
                 'execute': {'execute_trajectory', 'check_success'}}[self.phase]
        result = [copy.deepcopy(t) for t in TOOLS if t['function']['name'] in names]
        for tool in result:
            fn = tool['function']
            if fn['name'] == 'solve_constraint':
                fn['parameters']['properties']['relation']['enum'] = [self.relation]
                fn['description'] = 'Plan the current approach using relation=%s. Returns a trajectory ID; then execute it.' % self.relation
            elif fn['name'] == 'execute_trajectory':
                fn['parameters']['properties']['traj']['enum'] = [self.traj]
        return result

    def validate(self, name, args):
        tools = {t['function']['name']:t['function']['parameters'] for t in self.tools()}
        if name not in tools:
            raise ValueError('Tool not allowed in phase=' + self.phase)
        schema = tools[name]
        if not isinstance(args, dict) or set(args) != set(schema['required']):
            raise ValueError('Tool argument keys do not match schema')
        for key, value in args.items():
            prop = schema['properties'][key]
            if prop['type'] == 'string' and not isinstance(value,str):
                raise ValueError('Expected string argument ' + key)
            if prop['type'] == 'array' and (not isinstance(value,list) or len(value)!=4 or any(type(x) is not int for x in value)):
                raise ValueError('Expected bbox of four integers')
            if 'enum' in prop and value not in prop['enum']:
                raise ValueError('Argument %s must be one of %s' % (key, prop['enum']))

    def record(self, name, args, result):
        before = self.phase
        reason = None
        if 'error' in result:
            signature = name + ':' + str(result['error'])
            self.error_counts[signature] = self.error_counts.get(signature,0) + 1
            self.last_error = {'tool':name, 'arguments':args, 'error':result['error']}
            if self.error_counts[signature] >= 2:
                reason = 'REPEAT_REVIEW: same invalid call repeated twice'
        elif name == 'track_keypoint' and self.phase == 'track':
            self.phase = 'plan'
        elif name == 'solve_constraint' and result.get('traj'):
            self.traj = result['traj']
            self.phase = 'execute'
        elif name == 'execute_trajectory':
            self.executions += 1
            self.traj = None
            self.phase = 'plan'
        self.no_progress = self.no_progress+1 if self.phase == before else 0
        if self.no_progress >= 2:
            reason = reason or 'REPEAT_REVIEW: two tool calls without workflow progress'
        return reason

    def summary(self):
        return {'phase':self.phase, 'executions':self.executions,
                'legal_relation':self.relation if self.phase=='plan' else None,
                'pending_traj':self.traj, 'no_progress_calls':self.no_progress,
                'last_error':self.last_error}
