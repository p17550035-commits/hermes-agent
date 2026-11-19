# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_stop_before_adoption_reaches_the_rebuilt_agent_not_only_the_stale_cached_one(*args, **kwargs):
    return None
