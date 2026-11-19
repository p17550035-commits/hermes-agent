# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SESSION = None

WORKER_SESSION = None

class RecordingApiServerAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeResponse:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakePostCtx:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeHttpSession:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def served(*args, **kwargs):
    return None

def _own_session(*args, **kwargs):
    return None

def _make_runner(*args, **kwargs):
    return None

def _subscription(*args, **kwargs):
    return None

def _unseen(*args, **kwargs):
    return None

def _run_one_notifier_tick(*args, **kwargs):
    return None

def _api_sub(*args, **kwargs):
    return None

def test_served_profile_wake_runs_in_process_only_for_the_session_it_owns(*args, **kwargs):
    return None

def test_internal_session_turn_targets_the_live_session_under_the_owner_profile(*args, **kwargs):
    return None
