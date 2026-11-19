# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _quiet_bool(*args, **kwargs):
    return None

def _mgr_call(*args, **kwargs):
    return None

class GatewayGoalCommandsMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
