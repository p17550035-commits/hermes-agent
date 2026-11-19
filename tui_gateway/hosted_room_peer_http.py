# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_NOT_ADMITTED_ERRNOS = None

_ERROR_CODE_RE = None

MAX_PEER_RESPONSE_BYTES = None

MAX_PEER_ERROR_RESPONSE_BYTES = None

_PEER_RESPONSE_CHUNK_BYTES = None

_RECEIPT_SCOPE_FIELDS = None

_TERMINAL_RUN_STATES = None

_ACTIVE_RUN_STATES = None

_KNOWN_RUN_STATES = None

_RUN_STATUS_KEYS = None

_LEGACY_DISPATCH_MESSAGE_CODES = None

_GRANT_RENEWAL_CODES = None

_EXECUTION_POLICY_CHANGED = None

_CAPABILITY_CHANGED = None

_REAUTHORIZATION_CODES = None

_REAUTHORIZATION_MESSAGES = None

_BUDGET_MESSAGES = None

class _PeerResponseTooLarge:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _PeerResponseDeadlineExceeded:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _set_response_socket_timeout(*args, **kwargs):
    return None

def _read_bounded_response(*args, **kwargs):
    return None

def _read_body(*args, **kwargs):
    return None

def _is_proven_pre_admission_failure(*args, **kwargs):
    return None

def _valid_code(*args, **kwargs):
    return None

def _response_error_code(*args, **kwargs):
    return None

class PeerRunsHTTPError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def digest_reauthorization_error(*args, **kwargs):
    return None

def _run_path(*args, **kwargs):
    return None

def _run_status(*args, **kwargs):
    return None

class PeerRunsHTTPClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
