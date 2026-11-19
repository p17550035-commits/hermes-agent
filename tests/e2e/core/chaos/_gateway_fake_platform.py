# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PLATFORM_NAME = None

PLUGIN_DIR_NAME = None

ALLOW_ALL_ENV = None

PORT_ENV = None

HEARTBEAT_TICK_S = None

HEARTBEAT_REPORT_S = None

class ChaosFakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def register(*args, **kwargs):
    return None
