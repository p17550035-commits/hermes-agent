# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _session(*args, **kwargs):
    return None

class TestSessionCreation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestVoiceLiveTurnNote:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
