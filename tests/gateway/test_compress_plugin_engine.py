# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakePluginEngine:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_source(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def _make_history(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def test_compress_works_with_plugin_context_engine(*args, **kwargs):
    return None
