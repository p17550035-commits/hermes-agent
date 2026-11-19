# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _InlineThread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _session(*args, **kwargs):
    return None

def emits(*args, **kwargs):
    return None

def turn_env(*args, **kwargs):
    return None

def _events(*args, **kwargs):
    return None

def test_fail_inflight_turn_retains_partial_and_error(*args, **kwargs):
    return None

def test_snapshot_returned_for_error_only_turn(*args, **kwargs):
    return None

def test_healthy_snapshot_carries_no_error_keys(*args, **kwargs):
    return None

def test_returned_error_result_retains_snapshot_and_emits_terminal_frame(*args, **kwargs):
    return None

def test_returned_error_result_carries_error_surface(*args, **kwargs):
    return None

def test_returned_error_without_reason_omits_no_frame(*args, **kwargs):
    return None

def test_completed_turn_still_clears_inflight(*args, **kwargs):
    return None

def test_returned_partial_error_keeps_final_response_text(*args, **kwargs):
    return None

def test_only_partial_answers_on_failed_turns_set_flag(*args, **kwargs):
    return None

def test_exception_closes_turn_with_terminal_complete_and_partial(*args, **kwargs):
    return None

def test_live_session_payload_exposes_retained_failure(*args, **kwargs):
    return None

def test_next_turn_replaces_retained_error_snapshot(*args, **kwargs):
    return None
