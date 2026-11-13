"""Loaded only for this explicitly instrumented default CLI invocation."""
import os
artifacts = os.environ.pop('MEMORY_H2_RUN_ARTIFACTS', None)
if artifacts:
    try:
        from monitor import install
        install(artifacts,guard=True)
    except BaseException:
        raise SystemExit('Run-only monitor could not initialize; model was not started.')
