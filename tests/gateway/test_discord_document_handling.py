# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_discord_mock(*args, **kwargs):
    return None

class FakeDMChannel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _redirect_cache(*args, **kwargs):
    return None

def adapter(*args, **kwargs):
    return None

def make_attachment(*args, **kwargs):
    return None

def make_message(*args, **kwargs):
    return None

def _mock_aiohttp_download(*args, **kwargs):
    return None

class TestIncomingDocumentHandling:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestAllowAnyAttachment:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
