"""Run-only diagnostics and user-requested stop; no request-policy overrides."""
import hashlib
import json
from pathlib import Path


def install(out, *, guard=False):
    from go2_demo.models import APIModel, ModelProtocolError
    from go2_demo.runner import RunLog
    out = Path(out)
    if guard:
        root = Path('/home/nuonuosenlin/Agent-harness')
        config = json.loads((out/'config.json').read_text())
        hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in sorted((root/'go2_demo').glob('*.py'))}
        assert hashes == config['code_sha256'], 'Source changed after freeze'
        with (out/'started.json').open('x') as stream:
            json.dump({'entrypoint':'python -m go2_demo','request_policy':'default; at most two',
                       'consecutive_gate_stop':2},stream)
    bounded = APIModel._bounded_request
    once = APIModel._decide_once
    write = RunLog.write

    async def capture_body(self, payload, timeout_s):
        self._capture_request_seq = getattr(self,'_capture_request_seq',0)+1
        body = await bounded(self,payload,timeout_s)
        self._capture_body = bytes(body)
        return body

    def capture_error(self,*args,**kwargs):
        self._capture_body = None
        try:
            return once(self,*args,**kwargs)
        except ModelProtocolError as exc:
            errors = out/'protocol_errors'
            errors.mkdir(parents=True,exist_ok=True)
            number = getattr(self,'_capture_error_seq',0)+1
            self._capture_error_seq = number
            request = getattr(self,'_capture_request_seq',0)
            observation = args[0] if args else kwargs.get('observation',{})
            step = observation.get('memory_state',{}).get('world',{}).get('decision_step')
            metadata = {'error_index':number,'request_sequence':request,
                'decision':step+1 if isinstance(step,int) else None,
                'error_code':exc.code,'message':str(exc),
                'diagnostic':getattr(self,'_last_protocol_metadata',None),
                'body_available':self._capture_body is not None}
            if self._capture_body is not None:
                raw = self._capture_body
                safe = raw
                # Never persist a credential if a provider unexpectedly echoes it.
                if self._api_key:
                    safe = safe.replace(self._api_key.encode(),b'[REDACTED]')
                path = errors/f'{number:03d}-request{request:03d}.raw'
                with path.open('xb') as stream:
                    stream.write(safe)
                metadata.update(raw_response_file=str(path),original_bytes=len(raw),stored_bytes=len(safe),
                    original_sha256=hashlib.sha256(raw).hexdigest(),stored_sha256=hashlib.sha256(safe).hexdigest(),
                    credential_redaction=(safe!=raw))
                if isinstance(metadata['diagnostic'],dict):
                    metadata['diagnostic']['raw_response_file']=str(path)
            with (errors/'captures.jsonl').open('a',encoding='utf-8') as stream:
                stream.write(json.dumps(metadata,ensure_ascii=False)+'\n')
            raise

    def stop_monitor(self,event,**data):
        write(self,event,**data)
        if event!='tool_results':
            return
        rejected = any(r.get('error_code') in {'MEMORY_CONSTRAINT','MEMORY_NO_PROGRESS'}
                       for r in data.get('results',[]))
        self._gate_streak = getattr(self,'_gate_streak',0)+1 if rejected else 0
        if self._gate_streak>=2:
            reason = {'reason':'consecutive_memory_gate_rejections','threshold':2,
                      'last_decision':data['turn']+1,'last_results':data['results'],
                      'episode':str(self.directory),'stop_before_next_model_request':True}
            with (out/'stop_reason.json').open('x',encoding='utf-8') as stream:
                stream.write(json.dumps(reason,ensure_ascii=False,indent=2)+'\n')
            # This occurs after tool feedback, memory submission, usage and logs.
            # The runner's normal interrupt path settles/stops and scores once.
            raise KeyboardInterrupt

    APIModel._bounded_request = capture_body
    APIModel._decide_once = capture_error
    RunLog.write = stop_monitor

    def undo():
        APIModel._bounded_request = bounded
        APIModel._decide_once = once
        RunLog.write = write
    return undo
