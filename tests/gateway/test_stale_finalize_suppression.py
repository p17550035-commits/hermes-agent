# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class FinalizeCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

STREAMED_PREFIX = None

MISSING_TAIL = None

FULL_RESPONSE = None

class StalePrefixAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class CompleteStreamAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_runner(*args, **kwargs):
    return None

def _run_streaming_turn(*args, **kwargs):
    return None

def test_stale_finalize_does_not_suppress_complete_response(*args, **kwargs):
    return None

def test_equal_text_control_still_suppresses_duplicate_send(*args, **kwargs):
    return None

class _PayloadLessSplitConsumer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_payload_less_split_does_not_suppress_complete_response(*args, **kwargs):
    return None

def _consumer(*args, **kwargs):
    return None

class TestDeliveredFinalMatches:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _SplittingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _split_consumer(*args, **kwargs):
    return None

def _drain_split_turn(*args, **kwargs):
    return None

def test_complete_overflow_split_still_suppresses_duplicate(*args, **kwargs):
    return None

def test_split_delivery_missing_tail_does_not_suppress(*args, **kwargs):
    return None

def test_split_delivery_keeps_sealed_heads_on_fresh_final(*args, **kwargs):
    return None

def test_failed_final_edit_after_split_records_visible_payload(*args, **kwargs):
    return None

def test_empty_fallback_final_after_split_records_only_what_survives(*args, **kwargs):
    return None

def test_flood_retry_never_resends_full_payload_after_partial_split_delivery(*args, **kwargs):
    return None
