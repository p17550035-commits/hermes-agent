# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

BOOT_DEADLINE_S = None

SHUTDOWN_DEADLINE_S = None

PLUGIN_MANIFEST = None

PLUGIN_INIT = None

def gateway_extra_config(*args, **kwargs):
    return None

class Event:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class GatewayProc:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _suppress_oserror:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
