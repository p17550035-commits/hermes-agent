# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

class ServerRequest:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_lock = None

def can_replay_request(*args, **kwargs):
    return None

NOT_SHOWN_CODE = None

NOT_SHOWN_MESSAGE = None

def bind_sinks(*args, **kwargs):
    return None

def advertise(*args, **kwargs):
    return None

def forget(*args, **kwargs):
    return None

def answers_requests(*args, **kwargs):
    return None

def _unanswerable(*args, **kwargs):
    return None

def _emit_cancel(*args, **kwargs):
    return None

def _register(*args, **kwargs):
    return None

def send(*args, **kwargs):
    return None

def send_async(*args, **kwargs):
    return None

def _is_not_shown(*args, **kwargs):
    return None

def _decline(*args, **kwargs):
    return None

def resolve_response(*args, **kwargs):
    return None

def lock_answer(*args, **kwargs):
    return None

def cancel(*args, **kwargs):
    return None

def open_requests(*args, **kwargs):
    return None

def open_request_count(*args, **kwargs):
    return None

def pending_kind(*args, **kwargs):
    return None

def resolve_pinned_response(*args, **kwargs):
    return None

def is_response_frame(*args, **kwargs):
    return None

def reset_for_tests(*args, **kwargs):
    return None
