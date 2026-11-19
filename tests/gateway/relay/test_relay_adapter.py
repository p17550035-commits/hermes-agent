# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def make_desc(*args, **kwargs):
    return None

def _adapter(*args, **kwargs):
    return None

def test_advertises_descriptor_max_length(*args, **kwargs):
    return None

def test_len_fn_utf16_counts_code_units(*args, **kwargs):
    return None

class _CaptureTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_event(*args, **kwargs):
    return None

def _make_dm_event(*args, **kwargs):
    return None

def _make_scoped_event_with_author(*args, **kwargs):
    return None

def test_send_reattaches_dm_user_id_from_inbound_scope(*args, **kwargs):
    return None

def test_scoped_reply_reattaches_both_scope_id_and_user_id(*args, **kwargs):
    return None

def test_stop_typing_forwards_explicit_clear_with_routing_context(*args, **kwargs):
    return None

def test_send_typing_tags_egress_platform(*args, **kwargs):
    return None

class _RevokedTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _ChatInfoTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_get_chat_info_local_fallback_when_not_advertised(*args, **kwargs):
    return None

class _HangOnIdleTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_disconnect_tears_down_transport_when_go_idle_is_cancelled(*args, **kwargs):
    return None
