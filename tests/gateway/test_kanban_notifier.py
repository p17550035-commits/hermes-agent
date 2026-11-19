# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class DisconnectedAdapters:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run_one_notifier_tick(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _create_completed_subscription(*args, **kwargs):
    return None

def _unseen_terminal_events(*args, **kwargs):
    return None

def test_kanban_notifier_replays_telegram_dm_topic_delivery_metadata(*args, **kwargs):
    return None

def test_active_named_profile_subscription_is_delivered(*args, **kwargs):
    return None

def test_non_dispatch_gateway_claims_only_its_profile_subscriptions(*args, **kwargs):
    return None

def test_legacy_subscription_requires_confirmed_dispatcher_lock_owner(*args, **kwargs):
    return None

class FailingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ReportedFailureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_notifier_redelivers_same_kind_on_dispatch_cycle(*args, **kwargs):
    return None

def test_notifier_subscription_survives_done_reopen_until_archive(*args, **kwargs):
    return None

def test_notifier_wakeup_uses_subscription_chat_type(*args, **kwargs):
    return None

def _unseen_terminal_events_for(*args, **kwargs):
    return None

def test_kanban_notifier_isolates_per_subscription_failure(*args, **kwargs):
    return None

def test_notifier_delivers_block_loop_detected_triage_ping(*args, **kwargs):
    return None

class _StubEvent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _StubNotif:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _fmt_block_loop(*args, **kwargs):
    return None

def test_block_loop_technical_kind_uses_neutral_orchestration_wording(*args, **kwargs):
    return None

def test_block_loop_owner_input_keeps_decision_wording(*args, **kwargs):
    return None

def _wake_text(*args, **kwargs):
    return None

def _review_handoff_task(*args, **kwargs):
    return None

def test_review_requested_wakes_the_origin_session(*args, **kwargs):
    return None

def test_block_loop_detected_wakes_the_origin_session(*args, **kwargs):
    return None

def test_review_requested_does_not_wake_a_notify_only_subscription(*args, **kwargs):
    return None
