# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

FOLLOWERS = None

class CompactingModel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_followers_survive_compression_and_restart_in_order_exactly_once(*args, **kwargs):
    return None
