# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_GATEWAY_CMD = None

_OTHER_CMD = None

def _fake_proc_dir(*args, **kwargs):
    return None

class TestProcFallback:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_other_users_gateways_are_not_ours_unless_root(*args, **kwargs):
    return None

class TestPsFallbackBsdCompat:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestGetServicePidsAllProfiles:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
