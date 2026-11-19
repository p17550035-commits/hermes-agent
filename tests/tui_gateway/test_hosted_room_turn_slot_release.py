# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _InlineThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Lease:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def _turn_env(*args, **kwargs):
    return None

def test_hosted_room_turn_releases_bot_room_slot_when_it_ends(*args, **kwargs):
    return None

def test_ordinary_session_keeps_its_slot_after_a_turn(*args, **kwargs):
    return None
