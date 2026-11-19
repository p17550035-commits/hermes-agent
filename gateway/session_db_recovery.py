# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_INITIAL_RETRY_DELAY_SECONDS = None

_MAX_RETRY_DELAY_SECONDS = None

class _Unavailable:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _HealthSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_health_lock = None

_health_states = None

def _publish_health(*args, **kwargs):
    return None

def _registry_owned(*args, **kwargs):
    return None

class RecoverableHandleCache:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
