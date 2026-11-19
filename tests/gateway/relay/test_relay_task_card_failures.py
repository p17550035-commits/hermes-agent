# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class ExplodingTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

TASKS = None

class TestTaskCardTransportFailure:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
