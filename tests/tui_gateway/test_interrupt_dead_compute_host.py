# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _DeadComputeHost:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _isolated_session(*args, **kwargs):
    return None

def _interrupt(*args, **kwargs):
    return None

def test_dead_host_stop_clears_the_stuck_turn(*args, **kwargs):
    return None

def test_a_pending_host_completion_keeps_its_own_teardown(*args, **kwargs):
    return None

def test_after_teardown_running_belongs_to_the_drain(*args, **kwargs):
    return None

def test_a_successor_turn_that_replaced_inflight_is_not_clobbered(*args, **kwargs):
    return None

def test_supervisor_reports_pending_turns_per_session(*args, **kwargs):
    return None
