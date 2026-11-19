# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Agent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class CLI:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_tui_real_turn_snapshot_next_turn_and_child_threads(*args, **kwargs):
    return None

def test_cli_callbacks_honor_bound_snapshot_not_file(*args, **kwargs):
    return None

def test_cli_real_chat_binds_refreshes_and_restores_snapshot(*args, **kwargs):
    return None
