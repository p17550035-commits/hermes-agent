# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

SESSION_HEADER = None

TURN_HEADER = None

TOOL_CALL_HEADER = None

REQUEST_ID_HEADER = None

_OS_FAMILY = None

_EXPECTED_MISSES = None

class CallRef:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _platform_name(*args, **kwargs):
    return None

def request_surface(*args, **kwargs):
    return None

def user_agent(*args, **kwargs):
    return None

def _send_consented(*args, **kwargs):
    return None

def _conversation_id(*args, **kwargs):
    return None

def correlation_headers(*args, **kwargs):
    return None

def connector_headers(*args, **kwargs):
    return None

def response_request_id(*args, **kwargs):
    return None

def log_connector_outcome(*args, **kwargs):
    return None
