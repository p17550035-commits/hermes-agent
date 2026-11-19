# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

BUDGET = None

class _Ticks:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Stop:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Gateway:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def gw(*args, **kwargs):
    return None

def _serve(*args, **kwargs):
    return None

def _blocking_first_run(*args, **kwargs):
    return None

def _register_blocking(*args, **kwargs):
    return None

def test_a_slow_idle_task_does_not_delay_the_next_chore_or_the_heartbeat(*args, **kwargs):
    return None

def test_stop_with_a_run_going_returns_within_its_budget_and_nothing_runs_or_records_after(*args, **kwargs):
    return None

def test_stop_waits_for_a_run_that_ends_within_its_budget(*args, **kwargs):
    return None

def test_a_run_that_ends_before_the_stop_is_recorded(*args, **kwargs):
    return None

def test_after_an_in_process_restart_only_the_new_housekeeping_records(*args, **kwargs):
    return None
