# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

REQUEST_TIMEOUT_S = None

_POLL_S = None

class _Pending:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_lock = None

def owned_by(*args, **kwargs):
    return None

def may_settle(*args, **kwargs):
    return None

def is_response_frame(*args, **kwargs):
    return None

def resolve(*args, **kwargs):
    return None

def ask_viewer(*args, **kwargs):
    return None

def ask_viewer_result(*args, **kwargs):
    return None

def waiting(*args, **kwargs):
    return None

def open_requests(*args, **kwargs):
    return None

def withdraw(*args, **kwargs):
    return None

def lock_answer(*args, **kwargs):
    return None

def _ask(*args, **kwargs):
    return None
