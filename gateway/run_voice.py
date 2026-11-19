# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_VOICE_MODES = None

def _is_platform_name(*args, **kwargs):
    return None

def _is_legacy_voice_key(*args, **kwargs):
    return None

def _owner_voice_config(*args, **kwargs):
    return None

class GatewayVoiceMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
