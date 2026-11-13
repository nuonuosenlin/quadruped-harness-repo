"""One H2 episode only; capture the complete body on first protocol error.

The local source tree, observation, planning and evaluator remain untouched.
Only this run's explicit stop-on-error policy overrides the optional repair.
"""
from pathlib import Path
import hashlib
import json
import os
import sys

ROOT = Path('/home/nuonuosenlin/Agent-harness')
OUT = ROOT / 'runs/memory-v1-h2-rerun-20261111-s0'
sys.path.insert(0, str(ROOT))

from go2_demo.models import APIModel, ModelProtocolError


class CaptureAndStopModel(APIModel):
    def __init__(self, *args, capture_dir, **kwargs):
        super().__init__(*args, **kwargs)
        self.capture_dir = Path(capture_dir)
        self._raw_response = None

    async def _bounded_request(self, payload, timeout_s):
        body = await super()._bounded_request(payload, timeout_s)
        self._raw_response = bytes(body)
        return body

    def decide(self, *args, **kwargs):
        self._raw_response = None
        kwargs['max_requests'] = 1  # User's current stop condition: no repair request.
        try:
            return super().decide(*args, **kwargs)
        except ModelProtocolError as exc:
            self.capture_dir.mkdir(parents=True, exist_ok=True)
            metadata = {'error_code': exc.code, 'error_message': str(exc),
                        'protocol_diagnostics': getattr(exc, 'protocol_diagnostics', []),
                        'response_body_available': self._raw_response is not None,
                        'automatic_retry_sent': False}
            if self._raw_response is not None:
                raw = self._raw_response
                # Preserve all bytes/fields, except never write a credential.
                safe = raw
                for key in (self._api_key, os.environ.get('MODEL_API_KEY', '')):
                    if key:
                        safe = safe.replace(key.encode('utf-8'), b'[REDACTED]')
                path = self.capture_dir / 'response.raw'
                with path.open('xb') as stream:
                    stream.write(safe)
                metadata.update(response_body_file=str(path), original_byte_length=len(raw),
                    stored_byte_length=len(safe), original_sha256=hashlib.sha256(raw).hexdigest(),
                    stored_sha256=hashlib.sha256(safe).hexdigest(),
                    credential_redactions_applied=(safe != raw),
                    preservation='complete HTTP response body; credential-only redaction if required')
                if getattr(exc, 'protocol_diagnostics', None):
                    exc.protocol_diagnostics[-1]['raw_response_file'] = str(path)
            with (self.capture_dir / 'capture.json').open('x', encoding='utf-8') as stream:
                stream.write(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
            raise


def main():
    import go2_demo.__main__ as cli
    config = json.loads((OUT / 'config.json').read_text())
    current = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in sorted((ROOT / 'go2_demo').glob('*.py'))}
    assert current == config['code_sha256'], 'Source changed after configuration freeze'
    with (OUT / 'started.json').open('x') as stream:
        stream.write(json.dumps({'arm': 'H2', 'seed': 0, 'retry_on_protocol_error': False}) + '\n')

    def make_model(args, scenario):
        assert args.provider == config['provider'] and args.model_name == config['model']
        assert args.memory_v1 and args.seed == 0 and args.viewer
        assert scenario.task_id == config['task']
        return CaptureAndStopModel.from_env(provider=args.provider, api_key_file=args.api_key_file,
            model_name=args.model_name, trust_env=not args.no_env_proxy,
            timeout_s=args.api_timeout, history_turns=args.history_turns,
            max_output_tokens=args.max_output_tokens, capture_dir=OUT / 'protocol_error')

    cli._make_model = make_model
    return cli.main()


if __name__ == '__main__':
    raise SystemExit(main())
