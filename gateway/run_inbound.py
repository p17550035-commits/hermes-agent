# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_RELAY_MEDIA_PREFIX = None

_UNKNOWN_ATTACHMENT_NAME = None

def discord_triggering_note(*args, **kwargs):
    return None

def strip_discord_triggering_note(*args, **kwargs):
    return None

class GatewayInboundMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
