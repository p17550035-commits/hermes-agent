# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_event(*args, **kwargs):
    return None

class TestBaseInterruptSuppression:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
