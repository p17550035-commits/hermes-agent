# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

OWNER_PREFIX = None

TRANSPORT_PREFIX = None

_LIVE_ATTEMPT = None

_STOPPING = None

_ROOM_SESSION_CONFLICT = None

_ROOM_TITLE_CONFLICT = None

def _seated(*args, **kwargs):
    return None

def _task_allowed(*args, **kwargs):
    return None

def hosted_member_check(*args, **kwargs):
    return None

def _adopt_legacy_room(*args, **kwargs):
    return None

def _existing_room(*args, **kwargs):
    return None

def _create(*args, **kwargs):
    return None

class InMemoryHostedRoomRepository:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
