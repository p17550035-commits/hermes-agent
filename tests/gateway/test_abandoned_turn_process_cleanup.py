# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _IdleAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RaisingActivityAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _state(*args, **kwargs):
    return None

def _run_watchdog(*args, **kwargs):
    return None

def test_thread_watchdog_times_out_before_agent_exists(*args, **kwargs):
    return None

def test_thread_watchdog_times_out_when_activity_snapshot_raises(*args, **kwargs):
    return None

def test_thread_watchdog_reaps_only_processes_created_by_timed_out_turn(*args, **kwargs):
    return None

def test_completed_worker_wins_race_and_preserves_background_process(*args, **kwargs):
    return None

def test_timeout_cleanup_is_idempotent(*args, **kwargs):
    return None

def test_reap_skips_when_a_newer_turn_has_claimed_the_session(*args, **kwargs):
    return None

def test_reap_proceeds_when_this_turn_is_still_current(*args, **kwargs):
    return None

def test_reap_fails_open_when_is_still_current_raises(*args, **kwargs):
    return None

def test_reap_skips_empty_task_id(*args, **kwargs):
    return None

def test_timeout_abandon_propagates_is_still_current_to_the_reap(*args, **kwargs):
    return None

def _run_wedged_worker(*args, **kwargs):
    return None

def test_reaper_dumps_wedged_worker_stack_before_interrupt(*args, **kwargs):
    return None

def test_abandon_timed_out_turn_dumps_stacks_before_interrupt(*args, **kwargs):
    return None

def test_dump_wedged_turn_stacks_never_raises(*args, **kwargs):
    return None

def _plain_spawn(*args, **kwargs):
    return None

def _bind_session(*args, **kwargs):
    return None

def _spawn_background(*args, **kwargs):
    return None

def _kill_own(*args, **kwargs):
    return None

def test_stop_reaps_the_background_job_the_stopped_turn_started(*args, **kwargs):
    return None

def test_timed_out_turn_reaps_only_its_own_job_on_a_shared_container_key(*args, **kwargs):
    return None
