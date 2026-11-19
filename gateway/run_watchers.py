# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_SESSION_STORE_PRUNE_INTERVAL = None

_CACHE_EXPIRY_CONCURRENCY = None

def _interruptible_sleep(*args, **kwargs):
    return None

def drain_pending_cache_releases(*args, **kwargs):
    return None

class GatewaySessionWatchersMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
