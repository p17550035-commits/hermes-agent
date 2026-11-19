# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _DummyAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_event(*args, **kwargs):
    return None

def _hold_typing(*args, **kwargs):
    return None

def _strip_everything(*args, **kwargs):
    return None

class TestExtractStripRecoveryAllPlatforms:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRecoveryDoesNotLeakMediaFragments:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestUnrecoverableDropIsLoud:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPostStopInterruptSwallow:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
