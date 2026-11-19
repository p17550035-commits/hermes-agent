# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

class TranscriptReadError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _spool_dropped(*args, **kwargs):
    return None

_ASSISTANT_ONLY_KEYS = None

_BOUND_TEXT_KEYS = None

def _bindable_text(*args, **kwargs):
    return None

def transcript_append_kwargs(*args, **kwargs):
    return None

class SessionTranscriptMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
