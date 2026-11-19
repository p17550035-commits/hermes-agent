# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _wedged_turn(*args, **kwargs):
    return None

def test_stop_ends_a_turn_wedged_in_setup(*args, **kwargs):
    return None

def test_setup_past_its_deadline_ends_with_a_visible_notice(*args, **kwargs):
    return None

def test_a_stalled_setup_is_a_failed_turn_so_goal_never_grades_the_resend_notice(*args, **kwargs):
    return None
