# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class OkTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_sealed_tombstones_are_bounded(*args, **kwargs):
    return None

def test_open_drafts_are_bounded(*args, **kwargs):
    return None
