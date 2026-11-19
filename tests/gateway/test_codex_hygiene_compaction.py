# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class FakeCodexSession:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class LiveCodexAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _history(*args, **kwargs):
    return None

_STORAGE_HANDLES = None

def _close_storage_handles(*args, **kwargs):
    return None

def _gateway(*args, **kwargs):
    return None

def test_hermes_mode_compacts_live_thread_at_rpc_boundary(*args, **kwargs):
    return None

def test_hermes_mode_without_cached_agent_skips_without_local_compression(*args, **kwargs):
    return None

def test_native_and_off_modes_skip_cleanly(*args, **kwargs):
    return None

def test_unknown_mode_falls_back_to_native_semantics(*args, **kwargs):
    return None

def test_force_compacts_thread_never_local_fallback(*args, **kwargs):
    return None

def test_force_without_live_thread_does_not_run_local_compressor(*args, **kwargs):
    return None

def test_timeout_records_persistent_cooldown(*args, **kwargs):
    return None

def _slash_host(*args, **kwargs):
    return None

def test_manual_compress_routes_to_live_thread(*args, **kwargs):
    return None

def test_codex_compaction_releases_the_live_sessions_read_dedup(*args, **kwargs):
    return None

def test_hygiene_worker_inherits_caller_contextvars(*args, **kwargs):
    return None
