# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _replay_upload(*args, **kwargs):
    return None

def _check_quotas(*args, **kwargs):
    return None

def _hold_blob(*args, **kwargs):
    return None

def _commit_check(*args, **kwargs):
    return None

class InMemoryHostedRoomAttachmentRepository:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
