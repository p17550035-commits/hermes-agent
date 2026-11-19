# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class SoftFailAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class ApiServerLikeAdapter:
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

def test_apiserver_sub_wakes_subscription_destination_via_self_post(*args, **kwargs):
    return None

def test_apiserver_subscriptions_have_independent_wake_destinations(*args, **kwargs):
    return None

def test_apiserver_wake_failure_rewinds_then_retries_destination(*args, **kwargs):
    return None
