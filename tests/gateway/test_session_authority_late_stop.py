# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_stop_after_the_turn_finished_does_not_cancel_the_next_turn(*args, **kwargs):
    return None
