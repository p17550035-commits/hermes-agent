# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

MAX_STORED_RESPONSES = None

IDENTITY_RETENTION_FACTOR = None

_RECORD = None

def _locked(*args, **kwargs):
    return None

class ResponseStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
