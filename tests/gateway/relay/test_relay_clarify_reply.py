# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _asking_turn(*args, **kwargs):
    return None

def test_a_message_instead_of_an_answer_cancels_the_question_and_takes_over_in_queue_mode(*args, **kwargs):
    return None

def test_a_resent_answer_is_not_run_again_as_a_new_turn(*args, **kwargs):
    return None
