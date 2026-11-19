# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

WELCOME = None

PORTAL = None

def make_jwt(*args, **kwargs):
    return None

class FakePortal:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def install_portal(*args, **kwargs):
    return None

def as_local_desktop_backend(*args, **kwargs):
    return None

def off_local_desktop(*args, **kwargs):
    return None

def claimed_trial(*args, **kwargs):
    return None
