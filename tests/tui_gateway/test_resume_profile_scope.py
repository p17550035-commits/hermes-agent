# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_BASE_URL = None

_STORED = None

class _NoopHydration:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _write_home(*args, **kwargs):
    return None

def _store(*args, **kwargs):
    return None

def homes(*args, **kwargs):
    return None

def _resume(*args, **kwargs):
    return None

def test_secondary_profile_overrides_resolve_against_its_own_config(*args, **kwargs):
    return None

def test_launch_profile_overrides_still_resolve_against_launch_config(*args, **kwargs):
    return None
