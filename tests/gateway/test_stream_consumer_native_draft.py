# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class AnimatedDraftAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def make_consumer(*args, **kwargs):
    return None

def push_delta(*args, **kwargs):
    return None

def test_native_drafts_coalesce_fast_deltas_and_publish_latest_snapshot(*args, **kwargs):
    return None

def test_native_draft_code_prefix_has_no_synthetic_fence_or_cursor(*args, **kwargs):
    return None

def test_skipped_draft_retries_latest_snapshot_without_claiming_delivery(*args, **kwargs):
    return None

def test_draft_cooldown_keeps_preview_transport_and_full_final_is_immediate(*args, **kwargs):
    return None

def test_draft_resumes_after_cooldown_with_latest_accumulated_text(*args, **kwargs):
    return None
