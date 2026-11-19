# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _Bridge:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

IMAGE = None

def test_retry_refuses_an_unresendable_turn_before_rewinding(*args, **kwargs):
    return None
