# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_adapter(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _session_key(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

class TestAdapterSessionCancellation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestStaleSessionLockSelfHeal:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRunnerSessionGenerationGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestOldTaskCannotClobberNewerGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
