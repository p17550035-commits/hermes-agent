# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

FAST_OVERRIDES = None

def _agent(*args, **kwargs):
    return None

def _set(*args, **kwargs):
    return None

def _get(*args, **kwargs):
    return None

class TestConfigSetFastSessionScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestConfigGetFastSessionScope:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSessionInfoFastFollowsTheRoute:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
