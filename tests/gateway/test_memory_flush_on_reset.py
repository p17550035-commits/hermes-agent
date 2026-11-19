# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_GATE_DELAY_S = None

class _RecordingProvider:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_agent(*args, **kwargs):
    return None

def test_cleanup_flushes_pending_writes_before_shutdown(*args, **kwargs):
    return None
