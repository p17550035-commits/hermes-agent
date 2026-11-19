# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

CHILD_ENV_KEYS = None

def child_env(*args, **kwargs):
    return None

def rpc(*args, **kwargs):
    return None

def websocket(*args, **kwargs):
    return None

def seed_offline_models_dev(*args, **kwargs):
    return None

def daemon(*args, **kwargs):
    return None

def probe(*args, **kwargs):
    return None
