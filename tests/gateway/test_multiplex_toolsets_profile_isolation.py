# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

aiohttp = None

OWNER_KEY = None

LOKAJ_KEY = None

def hermes_root(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

def _make_app(*args, **kwargs):
    return None

def _enabled_toolsets(*args, **kwargs):
    return None

class TestMultiplexOnToolsetIsolation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMultiplexOffPrefixFailsClosed:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestWebhookMultiplexOffPrefixFailsClosed:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
