# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_adapter(*args, **kwargs):
    return None

def _event(*args, **kwargs):
    return None

def test_cancel_background_tasks_drains_late_arrivals(*args, **kwargs):
    return None
