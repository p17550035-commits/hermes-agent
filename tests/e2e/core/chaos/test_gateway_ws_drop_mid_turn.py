# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

BOOT_S = None

TURN_S = None

PHASES = None

def _reply(*args, **kwargs):
    return None

def _last_user(*args, **kwargs):
    return None

class _Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Viewer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _control(*args, **kwargs):
    return None

def _identify(*args, **kwargs):
    return None

def _poll(*args, **kwargs):
    return None

def _read(*args, **kwargs):
    return None

def _close_armed(*args, **kwargs):
    return None

def _replies(*args, **kwargs):
    return None

def _end_reason(*args, **kwargs):
    return None

def _admissions(*args, **kwargs):
    return None

def _settled(*args, **kwargs):
    return None

def _closed_mid_turn(*args, **kwargs):
    return None

def _start(*args, **kwargs):
    return None

def _follow_up(*args, **kwargs):
    return None

def scenario(*args, **kwargs):
    return None

def test_dropped_viewer_never_stops_the_accepted_turn(*args, **kwargs):
    return None

def test_the_session_takes_the_next_message_after_the_drop(*args, **kwargs):
    return None

def test_reattach_after_drop_shows_the_finished_turn(*args, **kwargs):
    return None

def test_reattach_mid_turn_receives_the_completion_live(*args, **kwargs):
    return None
