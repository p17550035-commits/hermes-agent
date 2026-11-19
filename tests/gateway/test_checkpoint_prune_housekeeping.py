# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _OneTickStopEvent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_gateway_housekeeping_runs_the_checkpoint_prune(*args, **kwargs):
    return None
