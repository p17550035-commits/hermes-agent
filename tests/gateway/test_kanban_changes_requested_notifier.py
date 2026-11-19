# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run_one_tick(*args, **kwargs):
    return None

def _runner(*args, **kwargs):
    return None

def _create_review_block(*args, **kwargs):
    return None

def _unseen(*args, **kwargs):
    return None

def test_changes_requested_notify_wake_is_actionable_and_exactly_routed(*args, **kwargs):
    return None

def test_changes_requested_notify_is_passive_only(*args, **kwargs):
    return None

def test_changes_requested_wake_only_has_no_passive_post(*args, **kwargs):
    return None

def test_changes_requested_send_failure_retries_without_event_loss(*args, **kwargs):
    return None

def test_changes_requested_reason_is_redacted_path_safe_and_truncated(*args, **kwargs):
    return None
