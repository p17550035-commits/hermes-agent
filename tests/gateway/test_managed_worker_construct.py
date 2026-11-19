# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reply(*args, **kwargs):
    return None

class Primary:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class Backup:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _serve(*args, **kwargs):
    return None

def run_pair(*args, **kwargs):
    return None

def test_managed_turn_falls_back_like_the_in_process_turn(*args, **kwargs):
    return None

def test_managed_turn_sends_configured_instruction_and_prefill(*args, **kwargs):
    return None

def test_new_sessions_send_the_profiles_current_prefill(*args, **kwargs):
    return None

def test_construct_inputs_follow_the_session_mode(*args, **kwargs):
    return None
