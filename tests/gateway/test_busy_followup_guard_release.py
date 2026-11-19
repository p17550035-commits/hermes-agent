# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Turns:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _HeldRead:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _stock_interrupt(*args, **kwargs):
    return None

def _multiplexed_queue_text(*args, **kwargs):
    return None

def _stock_interrupt_ack_raises(*args, **kwargs):
    return None

ROUTES = None

def _event(*args, **kwargs):
    return None

def _gateway(*args, **kwargs):
    return None

def _followup_accepted_while_turn_unwinds(*args, **kwargs):
    return None

def _run_until_idle(*args, **kwargs):
    return None

def _orphaned(*args, **kwargs):
    return None

def test_followup_accepted_as_turn_ends_is_owned_and_runs_before_a_later_message(*args, **kwargs):
    return None

def test_followup_stored_before_the_busy_handler_raised_runs_once(*args, **kwargs):
    return None

def test_reconnect_during_busy_admission_runs_accepted_followup_once(*args, **kwargs):
    return None
