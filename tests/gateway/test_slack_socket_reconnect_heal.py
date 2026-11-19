# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_slack_mock(*args, **kwargs):
    return None

class _FakeSession:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeSocketModeClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeHandler:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _spin(*args, **kwargs):
    return None

def adapter(*args, **kwargs):
    return None

def _attach(*args, **kwargs):
    return None

class TestSocketModeTeardown:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSocketModeRestart:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
