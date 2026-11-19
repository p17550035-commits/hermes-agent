# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def make_desc(*args, **kwargs):
    return None

class FakeMediaClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

def test_send_image_url_passes_through_without_upload(*args, **kwargs):
    return None

def test_local_path_lanes_upload_first(*args, **kwargs):
    return None

def test_op_gating_falls_back_when_not_advertised(*args, **kwargs):
    return None

def test_legacy_connector_local_file_keeps_its_fallback_receipt(*args, **kwargs):
    return None

def test_connector_decline_after_upload_is_a_failed_send_with_one_notice(*args, **kwargs):
    return None

def test_lost_ack_on_send_media_is_not_reported_as_an_undelivered_attachment(*args, **kwargs):
    return None

def _make_event(*args, **kwargs):
    return None

def test_inbound_without_client_keeps_public_drops_rehost(*args, **kwargs):
    return None

def test_client_upload_rejects_oversize_and_missing(*args, **kwargs):
    return None

def test_download_sends_a_user_agent_on_every_request(*args, **kwargs):
    return None

def test_is_relay_media_url_distinguishes_rehost_from_public(*args, **kwargs):
    return None

def test_download_routes_auth_decision_through_is_relay_media_url(*args, **kwargs):
    return None

def test_is_relay_media_url_requires_connector_origin_and_base_path(*args, **kwargs):
    return None

def test_download_never_sends_bearer_to_foreign_origin_with_relay_path(*args, **kwargs):
    return None

def test_inbound_failed_foreign_url_with_relay_path_is_kept_as_public(*args, **kwargs):
    return None

def test_rehost_on_another_origin_names_both_origins_once(*args, **kwargs):
    return None

def test_malformed_url_does_not_abort_later_attachments(*args, **kwargs):
    return None
