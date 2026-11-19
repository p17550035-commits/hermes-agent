# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_DEFAULT_TOOL_GATEWAY_DOMAIN = None

_DEFAULT_TOOL_GATEWAY_SCHEME = None

_NOUS_ACCESS_TOKEN_REFRESH_SKEW_SECONDS = None

class ManagedToolGatewayConfig:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _clean(*args, **kwargs):
    return None

def auth_json_path(*args, **kwargs):
    return None

def _read_nous_provider_state(*args, **kwargs):
    return None

def _read_user_token_override(*args, **kwargs):
    return None

def peek_nous_access_token(*args, **kwargs):
    return None

def read_nous_access_token(*args, **kwargs):
    return None

def _replace_dead_guest_token(*args, **kwargs):
    return None

def get_tool_gateway_scheme(*args, **kwargs):
    return None

def build_vendor_gateway_url(*args, **kwargs):
    return None

def _vendor_gateway(*args, **kwargs):
    return None

def resolve_managed_tool_gateway(*args, **kwargs):
    return None

def resolve_free_search_gateway(*args, **kwargs):
    return None

def is_managed_tool_gateway_ready(*args, **kwargs):
    return None
