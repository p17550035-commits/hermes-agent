# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_tool_call_logger_lock = None

def _tool_call_logger(*args, **kwargs):
    return None

_CONTEXT_OVERFLOW_ERROR_PHRASES = None

def _unexpected_silence_reply(*args, **kwargs):
    return None

def is_context_overflow_failure_result(*args, **kwargs):
    return None

_HYGIENE_SETUP_ROLES = None

def bound_model_input_without_hygiene(*args, **kwargs):
    return None

def hygiene_no_commit_reason(*args, **kwargs):
    return None

class GatewayTurnMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
