# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_RESTART_NOTICE_TTL_SECONDS = None

def _notice_expired(*args, **kwargs):
    return None

class GatewayRestartNoticeMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
