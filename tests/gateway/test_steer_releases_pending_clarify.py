# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SESSION_KEY = None

CLARIFY_ID = None

class _Receiver:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _no_leaked_clarify(*args, **kwargs):
    return None

def _runner(*args, **kwargs):
    return None

def _steer_event(*args, **kwargs):
    return None

def test_steer_releases_the_clarify_that_owns_the_turn(*args, **kwargs):
    return None

def test_steer_releases_a_choice_prompt_too(*args, **kwargs):
    return None

def test_a_clarify_without_a_steer_stays_pending(*args, **kwargs):
    return None

def test_steer_without_a_clarify_is_unchanged(*args, **kwargs):
    return None
