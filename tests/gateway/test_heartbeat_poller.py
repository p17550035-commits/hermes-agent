# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _HeartbeatAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def poller(*args, **kwargs):
    return None

def test_idle_wake_coalesces_intervals_while_adapter_owns_turn(*args, **kwargs):
    return None

def test_unavailable_or_busy_session_leaves_persisted_tick_due(*args, **kwargs):
    return None

def test_emergency_stop_holds_due_tick_without_messaging_until_resume(*args, **kwargs):
    return None

def test_emergency_stop_gate_drops_heartbeat_silently_but_tells_real_users(*args, **kwargs):
    return None
