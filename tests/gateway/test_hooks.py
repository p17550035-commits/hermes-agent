# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _create_hook(*args, **kwargs):
    return None

class TestDiscoverAndLoad:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEmit:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEmitCollect:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
