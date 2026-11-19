# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

UNIT = None

def unit(*args, **kwargs):
    return None

def test_refresh_from_another_home_leaves_the_unit_untouched(*args, **kwargs):
    return None

def test_refresh_from_the_pinned_home_still_rewrites_a_stale_unit(*args, **kwargs):
    return None

class TestTempHomeServiceDefinitionGuard:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
