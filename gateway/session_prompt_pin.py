# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROMPT_PIN_VERSION = None

def sanitize_prompt_pin(*args, **kwargs):
    return None

class SessionPromptPinMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
