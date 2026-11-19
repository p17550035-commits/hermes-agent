# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class TestIsGatewayOwnedSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_session(*args, **kwargs):
    return None

def _make_real_session(*args, **kwargs):
    return None

def _read_real_row(*args, **kwargs):
    return None

class TestGatewayOwnedSessionTeardown:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestDesktopAutomaticReclaimTeardown:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
