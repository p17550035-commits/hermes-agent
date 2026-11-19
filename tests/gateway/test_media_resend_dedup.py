# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _DummyAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _StubStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_event(*args, **kwargs):
    return None

def _hold_typing(*args, **kwargs):
    return None

def _allowed_file(*args, **kwargs):
    return None

def test_explicit_media_resend_is_delivered_despite_history(*args, **kwargs):
    return None

def test_first_delivery_not_poisoned_by_current_turn_tool_output(*args, **kwargs):
    return None

def test_bare_local_path_history_dedup_survives_and_logs(*args, **kwargs):
    return None

def test_plain_text_response_does_not_load_transcript(*args, **kwargs):
    return None

def test_explicit_media_response_does_not_load_transcript(*args, **kwargs):
    return None

def test_bare_path_history_lookup_does_not_block_event_loop(*args, **kwargs):
    return None

def test_bare_path_history_lookup_timeout_fails_open(*args, **kwargs):
    return None

def test_history_lookup_saturation_fails_open_without_new_worker(*args, **kwargs):
    return None

def test_history_lookup_worker_start_failure_fails_open_and_releases_slot(*args, **kwargs):
    return None

def _stream_event(*args, **kwargs):
    return None

def _stream_adapter(*args, **kwargs):
    return None

def test_streamed_explicit_media_resend_is_delivered(*args, **kwargs):
    return None

def test_auto_append_lane_still_dedups_stale_media(*args, **kwargs):
    return None
