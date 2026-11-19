# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

def _bg_prompt_preview(*args, **kwargs):
    return None

class GatewayBackgroundMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
