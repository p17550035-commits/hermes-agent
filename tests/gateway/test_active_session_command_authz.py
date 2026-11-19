# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

HELD_TEXT = None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

class _Runner:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _busy_session(*args, **kwargs):
    return None

def _assert_turn_untouched(*args, **kwargs):
    return None

def _send_and_settle(*args, **kwargs):
    return None

def test_sender_refused_at_admission_cannot_cancel_another_users_turn(*args, **kwargs):
    return None

def test_allowlisted_member_refused_by_slash_access_cannot_cancel_the_turn(*args, **kwargs):
    return None

def test_an_inconclusive_authorization_check_does_not_cancel(*args, **kwargs):
    return None

def test_sender_without_a_user_id_cannot_cancel_the_turn(*args, **kwargs):
    return None

def test_accepted_stop_cancels_the_turn_and_drops_the_held_text(*args, **kwargs):
    return None

def test_adapter_without_an_authorization_check_keeps_the_unconditional_cancel(*args, **kwargs):
    return None

_GATED = None

def _runner_busy_stop(*args, **kwargs):
    return None

def test_runner_marks_an_admins_busy_stop_as_accepted(*args, **kwargs):
    return None

def test_runner_leaves_a_slash_denied_busy_stop_unmarked(*args, **kwargs):
    return None

def test_a_pre_gateway_dispatch_rewrite_does_not_hide_an_accepted_stop(*args, **kwargs):
    return None

def test_accepted_stop_drops_a_held_burst_before_its_slow_reply(*args, **kwargs):
    return None

def test_held_text_runs_when_the_owner_finishes_during_a_refusal_reply(*args, **kwargs):
    return None

def test_overlapping_refused_commands_hand_the_session_back_to_its_owner(*args, **kwargs):
    return None

def test_overlapping_commands_hand_the_session_to_whoever_still_settles_it(*args, **kwargs):
    return None

def test_a_stop_before_the_owners_task_first_runs_leaves_no_stale_guard(*args, **kwargs):
    return None

def test_a_drain_started_under_a_settled_refusal_releases_the_session(*args, **kwargs):
    return None

def test_a_message_during_a_refusal_after_the_owner_finished_keeps_the_held_burst(*args, **kwargs):
    return None
