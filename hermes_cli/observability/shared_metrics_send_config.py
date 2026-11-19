# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

DEFAULT_ENDPOINT = None

_LOCAL_HOSTS = None

_warned_send_without_collection = None

class SendConfig:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _endpoint_is_safe(*args, **kwargs):
    return None

def resolve_send_config(*args, **kwargs):
    return None
