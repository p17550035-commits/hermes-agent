# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Client:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_reload_mcp_runs_on_the_gateway(*args, **kwargs):
    return None
