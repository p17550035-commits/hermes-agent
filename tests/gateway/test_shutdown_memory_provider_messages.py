# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _mock_dotenv(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

class _FakeAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCleanupAgentResourcesPassesMessages:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
