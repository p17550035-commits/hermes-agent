# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

MAX_REPLICA_ROOMS = None

MAX_REPLICA_EVENT_BYTES = None

_SYSTEM_ACTOR = None

def _control_event(*args, **kwargs):
    return None

def _replica_state(*args, **kwargs):
    return None

def _store_events(*args, **kwargs):
    return None

class InMemoryHostedRoomReplicaRepository:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
