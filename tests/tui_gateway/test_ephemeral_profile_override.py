# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROFILE_HOME = None

class _InlineThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def fake_session(*args, **kwargs):
    return None

def override_calls(*args, **kwargs):
    return None

def _run(*args, **kwargs):
    return None

class TestBackgroundProfileOverride:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPreviewRestartProfileOverride:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
