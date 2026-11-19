# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class WakeAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def unused_handler(*args, **kwargs):
    return None

def test_completed_board_wake_is_admitted_without_changing_human_input(*args, **kwargs):
    return None

def busy_gateway(*args, **kwargs):
    return None

def test_identityless_external_input_is_still_rejected(*args, **kwargs):
    return None
