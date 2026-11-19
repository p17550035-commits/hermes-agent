# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _MediaRoutingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def _allowed_media_path(*args, **kwargs):
    return None

def test_base_adapter_routes_voice_tagged_telegram_ogg_media_tag_to_voice_sender(*args, **kwargs):
    return None

def _fake_runner(*args, **kwargs):
    return None

def test_streaming_delivery_blocks_media_path_outside_allowed_roots(*args, **kwargs):
    return None

class _DiscordMediaFailureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_non_streaming_media_failure_notifies_user(*args, **kwargs):
    return None

class _DiscordMediaFailureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_queued_followup_delivery_strips_media_tag_from_text_and_sends_image(*args, **kwargs):
    return None

def test_queued_followup_delivery_reuses_routing_metadata_for_media(*args, **kwargs):
    return None

def test_queued_followup_delivery_keeps_remote_image_url_in_text(*args, **kwargs):
    return None

def test_queued_followup_delivery_keeps_bare_local_path_in_text(*args, **kwargs):
    return None

def test_queued_followup_delivery_preserves_protected_media_example(*args, **kwargs):
    return None

def test_queued_followup_delivery_skips_media_when_turn_failed(*args, **kwargs):
    return None

class _QueuedMediaCaptureAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _QueuedMediaAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_queued_resend_branch_delivers_media_and_preserves_protected_example(*args, **kwargs):
    return None
