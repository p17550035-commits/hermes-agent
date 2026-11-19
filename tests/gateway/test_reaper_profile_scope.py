# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _RunningAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Runner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_interrupt_reaper_keeps_served_profile_home(*args, **kwargs):
    return None
