# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_DROPPED_PEER_WINERRORS = None

def dropped_peer(*args, **kwargs):
    return None

class GuardedAccept:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def install_proactor_accept_guard(*args, **kwargs):
    return None
