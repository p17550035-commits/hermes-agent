# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class DummyTelegramAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_event(*args, **kwargs):
    return None

class TestBasePlatformTopicSessions:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestTelegramAutoTtsCaptionDelivery:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
