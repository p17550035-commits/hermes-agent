# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_IDENTITY_COLUMNS = None

_LINK_COLUMNS = None

_DUE_COLUMNS = None

_RECEIPT_COLUMNS = None

def _identity(*args, **kwargs):
    return None

def _superseded(*args, **kwargs):
    return None

def _live(*args, **kwargs):
    return None

def _drop_expired_reservations(*args, **kwargs):
    return None

def _delete_owed(*args, **kwargs):
    return None

def _owe_revoke(*args, **kwargs):
    return None

class InMemoryHostedRoomPeerRepository:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
