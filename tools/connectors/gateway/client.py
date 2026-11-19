# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

DEFAULT_TIMEOUT_SECONDS = None

EXECUTE_TIMEOUT_SECONDS = None

SEARCH_TIMEOUT_SECONDS = None

SCHEMAS_TIMEOUT_SECONDS = None

STORAGE_TIMEOUT_SECONDS = None

_STORAGE_CHUNK_BYTES = None

_STORAGE_PUT_ROUTE = None

_STORAGE_GET_ROUTE = None

_MAX_RETRIES = None

_RETRY_ONCE_STATUSES = None

_MAX_RETRY_AFTER_SECONDS = None

_EXECUTE_ROUTE = None

class _Reply:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class Transport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class StorageTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _default_transport(*args, **kwargs):
    return None

def _default_endpoint_resolver(*args, **kwargs):
    return None

def _default_header_provider(*args, **kwargs):
    return None

class ConnectorClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def return_to_args(*args, **kwargs):
    return None

def _route_key(*args, **kwargs):
    return None

def _result_dict(*args, **kwargs):
    return None

def _error_dict(*args, **kwargs):
    return None

def _call_failure(*args, **kwargs):
    return None

def _rejects_single_call_form(*args, **kwargs):
    return None

def _retry_wait(*args, **kwargs):
    return None

def _safe_json(*args, **kwargs):
    return None
