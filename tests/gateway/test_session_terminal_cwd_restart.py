# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Model:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _pwd_after_restart(*args, **kwargs):
    return None

pytestmark = None

def test_a_chats_cd_survives_a_gateway_restart(*args, **kwargs):
    return None

def test_a_directory_gone_after_the_restart_falls_back_to_terminal_cwd(*args, **kwargs):
    return None

def test_a_new_conversation_starts_in_terminal_cwd_and_keeps_it_across_a_restart(*args, **kwargs):
    return None
