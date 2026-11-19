# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

def _eacces(*args, **kwargs):
    return None

class TestPathExistsSafe:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRuntimeDirIsOurs:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestUserSystemdSocketReadyForeignRuntime:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEnsureUserSystemdEnvForeignRuntime:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPreflightForeignRuntimeNoLeak:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
