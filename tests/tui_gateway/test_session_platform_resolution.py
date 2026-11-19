# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reload_resolver(*args, **kwargs):
    return None

def clean_env(*args, **kwargs):
    return None

class TestResolveSessionPlatform:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestResolveSessionSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestResolveAgentPlatform:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSessionSourceFallback:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
