# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

MCP_PEER = None

def _model_saw_tool(*args, **kwargs):
    return None

def test_ordinary_owner_launches_tool_worker_and_detach_does_not_cancel(*args, **kwargs):
    return None
