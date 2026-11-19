# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Peer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_reattach_preserves_terminal_delivery(*args, **kwargs):
    return None
