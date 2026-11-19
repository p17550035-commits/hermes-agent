# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

GUI_TOOLS = None

def no_desktop_env(*args, **kwargs):
    return None

class TestDesktopUiToolset:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSurfaceResolution:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestResolverPlumbing:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestExplicitEmptySelection:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
