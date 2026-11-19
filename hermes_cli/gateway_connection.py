# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

RESUME_REFUSALS = None

RESUME_GONE = None

_KEY_NOT_TAKEN = None

class CallStopped:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _resume_plain(*args, **kwargs):
    return None

def lost_before(*args, **kwargs):
    return None

class SessionState:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class GatewayConnection:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
