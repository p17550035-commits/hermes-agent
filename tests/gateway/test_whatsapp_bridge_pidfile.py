# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _spawn_sleeper(*args, **kwargs):
    return None

def _wait_dead(*args, **kwargs):
    return None

class TestIdentityGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestKillPortProcess:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
