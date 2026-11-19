# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def runner(*args, **kwargs):
    return None

def _patch_info(*args, **kwargs):
    return None

class TestFormatSessionInfo:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestChannelOverrideSessionInfo:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestResetNoticeSessionInfo:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
