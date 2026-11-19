# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _hash_id(*args, **kwargs):
    return None

def _hash_sender_id(*args, **kwargs):
    return None

def _hash_chat_id(*args, **kwargs):
    return None

def _is_path_unsafe(*args, **kwargs):
    return None

_CHAT_TYPE_PREFIX = None

class SessionSource:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class SessionContext:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_PII_SAFE_PLATFORMS = None

def _should_redact_pii(*args, **kwargs):
    return None

def _slack_tools_loaded(*args, **kwargs):
    return None

def _discord_tools_loaded(*args, **kwargs):
    return None

_MAX_PROMPT_METADATA_CHARS = None

def _format_untrusted_prompt_value(*args, **kwargs):
    return None

def neutralize_untrusted_inline_text(*args, **kwargs):
    return None

_SLACK_TOOLS_NOTE = None

_SLACK_NO_TOOLS_NOTE = None

def _slack_platform_notes(*args, **kwargs):
    return None

def _discord_platform_notes(*args, **kwargs):
    return None

_STATIC_PLATFORM_NOTES = None

_PLATFORM_NOTES = None

def build_session_context_prompt(*args, **kwargs):
    return None

PERSISTABLE_MODEL_OVERRIDE_KEYS = None

def sanitize_model_override(*args, **kwargs):
    return None

class SessionEntry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def build_channel_continuity_note(*args, **kwargs):
    return None

def is_shared_multi_user_session(*args, **kwargs):
    return None

def label_shared_sender(*args, **kwargs):
    return None

def _session_key_namespace(*args, **kwargs):
    return None

def _canonical_participant(*args, **kwargs):
    return None

def build_session_key(*args, **kwargs):
    return None

class _SessionFlight:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RouteChecks:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RouteDecision:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class AsyncSessionStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class SessionStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def build_session_context(*args, **kwargs):
    return None
