# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_REUSE_FIXED_PORT = None

_EXCLUSIVE_FIXED_PORT = None

class GatewayAPIHandle:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class GatewayDashboardMount:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _listener_socket(*args, **kwargs):
    return None

def _listener_public_url(*args, **kwargs):
    return None

def start_gateway_api(*args, **kwargs):
    return None

def warm_gateway_dashboard(*args, **kwargs):
    return None

_SESSION_SOCKET_MODULE = None

def preload_session_socket(*args, **kwargs):
    return None

def await_session_socket_preload(*args, **kwargs):
    return None

def session_socket_handler(*args, **kwargs):
    return None

def stop_gateway_api(*args, **kwargs):
    return None

def _embedded_chat_enabled(*args, **kwargs):
    return None

def _restart_wait_read(*args, **kwargs):
    return None

def _restart_wait_socket_ticket(*args, **kwargs):
    return None

class GatewayRuntimeAPI:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
