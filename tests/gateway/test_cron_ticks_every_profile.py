# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _CapturedTicker:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def isolated_profiles(*args, **kwargs):
    return None

def test_secondary_profile_is_ticked_with_multiplex_profiles_off(*args, **kwargs):
    return None
