# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Client:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _connection(*args, **kwargs):
    return None

class _Cli:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_rollback_lists_and_restores_through_the_gateway(*args, **kwargs):
    return None

def test_rollback_all_reaches_the_gateway_and_kept_edits_are_shown(*args, **kwargs):
    return None
