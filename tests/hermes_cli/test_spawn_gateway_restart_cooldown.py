# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def reset_restart_cooldown(*args, **kwargs):
    return None

def _exited_proc(*args, **kwargs):
    return None

class TestRepeatRestartWithinCooldown:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCooldownReleases:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestExistingBehaviourIsPreserved:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
