# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class ToolGatewayError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class GatewayAuthError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class GatewayUnavailable:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class IdempotencyConflict:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class RateLimited:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def parse_gateway_error(*args, **kwargs):
    return None

SIDE_AGENT_HINT = None

CARD_HINT = None

EXPIRED_SIDE_AGENT_HINT = None

EXPIRED_CARD_HINT = None

EXPIRED_LINK_HINT = None

_HINTS = None

def render_connection_required(*args, **kwargs):
    return None

def _default_message(*args, **kwargs):
    return None
