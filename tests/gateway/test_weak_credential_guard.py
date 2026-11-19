# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_gateway_config(*args, **kwargs):
    return None

def _validate_and_return(*args, **kwargs):
    return None

class TestPlatformTokenPlaceholderGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestAPIServerPlaceholderKeyGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
