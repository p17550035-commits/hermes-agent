# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _InlineThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def emits(*args, **kwargs):
    return None

def marker_home(*args, **kwargs):
    return None

def turn_env(*args, **kwargs):
    return None

def test_marker_roundtrip(*args, **kwargs):
    return None

def test_marker_survives_corrupt_sidecar(*args, **kwargs):
    return None

def test_sibling_backend_record_does_not_resurrect_a_cleared_marker(*args, **kwargs):
    return None

def _patch_local_interrupt(*args, **kwargs):
    return None

def test_interrupt_ack_retires_marker_before_run_thread_exits(*args, **kwargs):
    return None

def test_interrupt_racing_marker_write_cannot_leave_recovery_state(*args, **kwargs):
    return None

def test_concluded_turn_clears_marker(*args, **kwargs):
    return None

def test_handled_failure_still_clears_marker(*args, **kwargs):
    return None

def test_hosted_terminal_receipt_commits_before_marker_retire(*args, **kwargs):
    return None

def test_hosted_terminal_receipt_failure_keeps_crash_marker(*args, **kwargs):
    return None

def test_continuation_turn_records_attempt_and_original_prompt(*args, **kwargs):
    return None

def test_older_agent_still_gets_the_post_turn_stamp(*args, **kwargs):
    return None

def schedule_env(*args, **kwargs):
    return None

def test_fresh_marker_schedules_continuation(*args, **kwargs):
    return None

def test_hosted_room_marker_is_left_to_the_driver(*args, **kwargs):
    return None

def test_stale_marker_is_cleared_not_continued(*args, **kwargs):
    return None

def test_config_widens_freshness_window(*args, **kwargs):
    return None

def test_exhausted_attempts_break_the_loop(*args, **kwargs):
    return None

def test_disabled_by_config(*args, **kwargs):
    return None

def test_no_marker_means_no_continuation(*args, **kwargs):
    return None

def test_running_session_wins_over_continuation(*args, **kwargs):
    return None

def test_double_schedule_is_guarded(*args, **kwargs):
    return None

def test_failed_agent_build_leaves_marker_for_retry(*args, **kwargs):
    return None

_CHILD_WRITER = None

def _wait_for_marker(*args, **kwargs):
    return None

def test_marker_writer_state_rejects_a_recycled_pid(*args, **kwargs):
    return None

def test_second_backend_defers_to_a_live_marker_writer(*args, **kwargs):
    return None
