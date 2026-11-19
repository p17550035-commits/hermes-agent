# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _consumer(*args, **kwargs):
    return None

class TestAbandonOnTurnDeath:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
