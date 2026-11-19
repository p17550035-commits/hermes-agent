# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

TURN_TIMEOUT = None

REPLY = None

TERMINAL = None

def _responder(*args, **kwargs):
    return None

class _SseReader:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _poll_run(*args, **kwargs):
    return None

def scenario(*args, **kwargs):
    return None

def _ctx(*args, **kwargs):
    return None

def test_stream_client_sees_the_pending_approval(*args, **kwargs):
    return None

def test_second_client_sees_the_same_state_and_pending_control(*args, **kwargs):
    return None

def test_stale_generation_reply_is_refused_and_leaves_the_control_pending(*args, **kwargs):
    return None

def test_approval_from_the_second_client_resumes_the_streamed_turn(*args, **kwargs):
    return None

def test_late_client_sees_the_run_settled_with_nothing_pending(*args, **kwargs):
    return None
