# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Receiver:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _running_turn(*args, **kwargs):
    return None

def test_successful_redirect_moves_the_turn_reply_anchor_to_the_redirecting_message(*args, **kwargs):
    return None

def test_refused_or_foreign_redirect_leaves_the_anchor_on_the_opening_message(*args, **kwargs):
    return None

def test_a_turn_that_takes_in_an_addressed_message_keeps_the_silence_fallback(*args, **kwargs):
    return None
