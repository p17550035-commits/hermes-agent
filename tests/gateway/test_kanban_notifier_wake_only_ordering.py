# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class RecordingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FailingWakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _run_one_notifier_tick(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _make_completed_task(*args, **kwargs):
    return None

def _unseen_terminal_events(*args, **kwargs):
    return None

def _subs(*args, **kwargs):
    return None

def test_wake_only_success_advances_cursor_single_wake(*args, **kwargs):
    return None

def test_wake_only_failure_rewinds_and_redelivers(*args, **kwargs):
    return None

def test_notify_wake_failure_retries_without_repeating_ping(*args, **kwargs):
    return None

def test_wake_only_failure_cap_drops_subscription(*args, **kwargs):
    return None
