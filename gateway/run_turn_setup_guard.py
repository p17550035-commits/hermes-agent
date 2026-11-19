# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_TIMEOUT = None

_STOPPED = None

STOP_GRACE_S = None

class PreagentSetupStopped:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class PreagentSetupTimeout:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def preagent_setup_guard(*args, **kwargs):
    return None

def cancel_preagent_setup(*args, **kwargs):
    return None

def run_preagent_setup(*args, **kwargs):
    return None

def pending_setup_busy_notice(*args, **kwargs):
    return None
