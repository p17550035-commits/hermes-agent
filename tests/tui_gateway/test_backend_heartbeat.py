# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

IDLE_S = None

def db(*args, **kwargs):
    return None

def _heartbeats(*args, **kwargs):
    return None

class TestBackendHeartbeatRefresher:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEntryAndWsWiring:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
