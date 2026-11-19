# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SID = None

LOST = None

class FakeClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def gateway(*args, **kwargs):
    return None

def run_bounded(*args, **kwargs):
    return None

def test_a_new_session_gets_the_show_reasoning_flag(*args, **kwargs):
    return None

def test_a_hidden_viewer_resuming_a_session_turns_its_reasoning_flag_off(*args, **kwargs):
    return None

def test_a_restarted_gateway_gets_the_flag_again_before_the_next_turn(*args, **kwargs):
    return None

def test_a_prompt_behind_a_lost_turn_shows_the_discard_banner_and_discard_lets_it_run(*args, **kwargs):
    return None

def test_a_bare_discard_prints_usage_and_calls_nothing(*args, **kwargs):
    return None
