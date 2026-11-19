# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_LoadKey = None

_Loader = None

def _plugin_scope_from_callable(*args, **kwargs):
    return None

def _caller_plugin_scope(*args, **kwargs):
    return None

class PlatformEntry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def core_ships_platform(*args, **kwargs):
    return None

class PlatformRegistry:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

platform_registry = None
