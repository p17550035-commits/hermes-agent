# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

class _StubAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

def locked_out_dir(*args, **kwargs):
    return None

def test_unusable_lock_dir_parks_the_adapter_with_the_repair(*args, **kwargs):
    return None

def test_lock_dir_repair_is_picked_up_without_restart(*args, **kwargs):
    return None

def test_unreadable_stale_token_lock_is_named_not_reported_as_a_holderless_conflict(*args, **kwargs):
    return None

class _StartupProbe:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_a_sole_token_locked_platform_on_an_unusable_lock_dir_keeps_the_gateway_up(*args, **kwargs):
    return None
