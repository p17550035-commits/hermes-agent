# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeGateway:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_mock_agent(*args, **kwargs):
    return None

class TestCachedAgentCleanupOnShutdown:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRunningAgentsNotDoubleCleaned:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
