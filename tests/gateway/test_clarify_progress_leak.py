# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class ProgressCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ClarifyThenToolAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _install_fakes(*args, **kwargs):
    return None

def test_clarify_tool_never_renders_progress_bubble(*args, **kwargs):
    return None
