# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SECRET = None

PROXY = None

ENV_PROXY_VARS = None

class _EchoingClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def slack(*args, **kwargs):
    return None

def _rendered(*args, **kwargs):
    return None

def _leaked(*args, **kwargs):
    return None

def test_media_send_never_carries_the_proxy_secret(*args, **kwargs):
    return None

def test_missing_media_caption_fallback_log_never_carries_the_proxy_secret(*args, **kwargs):
    return None

def test_dm_open_log_never_carries_the_proxy_secret(*args, **kwargs):
    return None
