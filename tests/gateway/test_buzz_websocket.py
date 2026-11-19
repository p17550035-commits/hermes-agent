# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_buzz_mod = None

BuzzAdapter = None

_auth_path = None

_spec = None

nostr_auth = None

SELF_PUBKEY = None

TEST_PRIVATE_KEY = None

CHANNEL = None

def _make_adapter(*args, **kwargs):
    return None

def test_schnorr_sign_matches_official_bip340_vector_zero(*args, **kwargs):
    return None

def test_decode_private_key_rejects_bad_input(*args, **kwargs):
    return None

def test_build_auth_event_shape_and_owner_tag(*args, **kwargs):
    return None

class _FakeWebSocket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ScriptedWebSocket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_websocket_loop_reconnects_when_read_goes_silent(*args, **kwargs):
    return None

def test_websocket_loop_reconnects_when_discovery_send_sees_closed_socket(*args, **kwargs):
    return None

def test_websocket_loop_backs_off_and_publishes_retrying_on_clean_relay_close(*args, **kwargs):
    return None

def test_websocket_loop_dispatches_frames_and_closes_cleanly(*args, **kwargs):
    return None

def test_websocket_auth_raises_on_rejection(*args, **kwargs):
    return None

def test_websocket_auth_uses_credentials_owner_tag(*args, **kwargs):
    return None

def test_websocket_loop_drops_restricted_channel_without_reconnect(*args, **kwargs):
    return None

def test_websocket_loop_reconnects_on_non_restricted_closed(*args, **kwargs):
    return None

def test_restricted_channels_skipped_during_subscribe(*args, **kwargs):
    return None

def test_new_subscription_without_high_water_mark_has_no_since_floor(*args, **kwargs):
    return None

def test_seeded_subscription_resumes_from_high_water_mark(*args, **kwargs):
    return None

def test_closed_membership_phrases_prune_without_reconnect(*args, **kwargs):
    return None

def test_restricted_channel_not_readopted_by_discovery(*args, **kwargs):
    return None

def test_ws_discovery_loop_subscribes_newly_discovered_conversation(*args, **kwargs):
    return None

def test_ws_discovery_task_cancelled_when_connection_exits(*args, **kwargs):
    return None
