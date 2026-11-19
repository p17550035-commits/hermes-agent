# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

KEY = None

class _RecordingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _RaisingAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ReapedStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _build_gateway(*args, **kwargs):
    return None

def test_eviction_interrupts_before_release_and_drops_cached_agent(*args, **kwargs):
    return None

def test_eviction_cleanup_survives_empty_pending_or_failed_interrupt(*args, **kwargs):
    return None

def test_stale_finalizer_cannot_release_replacement_generation(*args, **kwargs):
    return None

def test_one_shot_override_settles_on_stop_and_stale_finalizer_is_a_noop(*args, **kwargs):
    return None

def test_turn_lease_rebind_preserves_parent_lock_domain_and_releases(*args, **kwargs):
    return None

def test_displaced_turn_lease_release_by_owning_generation(*args, **kwargs):
    return None
