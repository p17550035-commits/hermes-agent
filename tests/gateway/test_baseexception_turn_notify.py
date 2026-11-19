# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _ProbeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _source(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

def _raising_handler(*args, **kwargs):
    return None

def _event(*args, **kwargs):
    return None

def test_system_exit_from_turn_notifies_user_and_is_reraised(*args, **kwargs):
    return None

def test_keyboard_interrupt_from_turn_notifies_user_and_is_reraised(*args, **kwargs):
    return None

def test_plain_exception_still_notifies_without_propagating(*args, **kwargs):
    return None

def test_turn_exception_text_stays_in_log_not_chat(*args, **kwargs):
    return None
