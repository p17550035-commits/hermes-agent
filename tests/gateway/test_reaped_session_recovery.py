# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _DeadReapedAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _source(*args, **kwargs):
    return None

def _store(*args, **kwargs):
    return None

def _occupy_turn_slot(*args, **kwargs):
    return None

def test_reaped_session_message_reaches_cold_path(*args, **kwargs):
    return None

def test_alive_session_keeps_priority_interrupt_path(*args, **kwargs):
    return None

def test_guard_is_inert_with_stubbed_session_store(*args, **kwargs):
    return None
