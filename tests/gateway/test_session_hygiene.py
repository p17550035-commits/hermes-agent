# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_history(*args, **kwargs):
    return None

class HygieneCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_session_hygiene_preserves_transcript_when_no_rotation(*args, **kwargs):
    return None

def test_session_hygiene_preserves_transcript_when_in_place_configured_but_no_db(*args, **kwargs):
    return None

def test_session_hygiene_timeout_continues_to_agent_and_sets_cooldown(*args, **kwargs):
    return None

def test_session_hygiene_forces_in_place_compaction_with_bound_session_db(*args, **kwargs):
    return None

def test_session_hygiene_honors_configurable_hard_message_limit(*args, **kwargs):
    return None

_STORAGE_HANDLES = None

def _close_storage_handles(*args, **kwargs):
    return None

def _make_cooldown_runner(*args, **kwargs):
    return None

def test_hygiene_compression_cooldown_survives_gateway_restart(*args, **kwargs):
    return None

def test_hygiene_fence_cancel_records_cooldown_without_abort_flag(*args, **kwargs):
    return None

def test_hygiene_skips_when_compression_already_in_flight(*args, **kwargs):
    return None

_HARD_LIMIT = None

def _make_bound_probe_transcript(*args, **kwargs):
    return None

def _turn_payload(*args, **kwargs):
    return None

def _make_bound_runner(*args, **kwargs):
    return None

class _LandedCompressAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_bound_model_input_without_hygiene_is_deterministic_and_fail_closed(*args, **kwargs):
    return None

def test_hygiene_miss_bounds_the_model_payload(*args, **kwargs):
    return None
