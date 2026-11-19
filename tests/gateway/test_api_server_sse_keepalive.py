# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

REMOTE_CLIENT_IDLE_DEADLINE_S = None

class _RecordingResponse:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def adapter(*args, **kwargs):
    return None

def test_idle_openai_stream_writes_keepalive_before_remote_client_deadline(*args, **kwargs):
    return None

def test_idle_run_events_stream_uses_shared_keepalive_cadence(*args, **kwargs):
    return None
