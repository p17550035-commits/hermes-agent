# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

DEFAULT_DATASET_NAME = None

_HERMES_VERSION = None

_REDACTION_BLOCKED_MESSAGE = None

_NO_TOKEN_MESSAGE = None

_TOKEN_ENV_VARS = None

class TraceRedactionError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _now_iso(*args, **kwargs):
    return None

def _redact(*args, **kwargs):
    return None

def _text_block(*args, **kwargs):
    return None

def _part_to_block(*args, **kwargs):
    return None

def _content_to_blocks(*args, **kwargs):
    return None

def _parse_tool_args(*args, **kwargs):
    return None

def _tool_calls_to_blocks(*args, **kwargs):
    return None

def _git_branch(*args, **kwargs):
    return None

def _assistant_message(*args, **kwargs):
    return None

def _tool_result_message(*args, **kwargs):
    return None

def _user_message(*args, **kwargs):
    return None

def build_trace_jsonl(*args, **kwargs):
    return None

def _resolve_hf_token(*args, **kwargs):
    return None

def _do_upload(*args, **kwargs):
    return None

def load_session_messages(*args, **kwargs):
    return None

def upload_session_trace(*args, **kwargs):
    return None
