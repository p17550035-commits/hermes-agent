# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_ROUTER_TASK = None

_ROUTER_MAX_TOKENS = None

def _member_roster(*args, **kwargs):
    return None

def _recent_messages(*args, **kwargs):
    return None

def ask_router(*args, **kwargs):
    return None

CLAIM_TTL_SECONDS = None

class RouterCalls:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
