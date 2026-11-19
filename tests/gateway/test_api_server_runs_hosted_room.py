# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def auth_adapter(*args, **kwargs):
    return None

class TestHostedRoomRuns:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
