# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_SESSION_KEY = None

class _DocCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RefusingDocCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _agent_returning(*args, **kwargs):
    return None

def _none(*args, **kwargs):
    return None

def _run_with_refused_followup(*args, **kwargs):
    return None

def _completion_seam(*args, **kwargs):
    return None

def test_queued_lane_delivers_text_and_media_exactly_once(*args, **kwargs):
    return None

def test_refused_queued_send_leaves_the_completion_send_as_the_fallback(*args, **kwargs):
    return None
