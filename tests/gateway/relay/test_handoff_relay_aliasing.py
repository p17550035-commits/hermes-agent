# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RelayStub:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _config_with(*args, **kwargs):
    return None

class TestHandoffRelayAliasing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCliHandoffFrontedSet:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
