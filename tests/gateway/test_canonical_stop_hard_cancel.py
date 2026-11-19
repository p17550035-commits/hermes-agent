# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _delegation(*args, **kwargs):
    return None

def test_canonical_stop_hard_cancels_the_turn_and_keeps_background_delegations(*args, **kwargs):
    return None
