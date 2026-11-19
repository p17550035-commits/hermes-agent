# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_EXEC_QUICK_COMMAND_TIMEOUT = None

def _stop_exec_tree(*args, **kwargs):
    return None

def _carry_replied_voice_answer(*args, **kwargs):
    return None

class GatewayInboundHooksMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
