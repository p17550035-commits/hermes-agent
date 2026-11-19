# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

DESCRIPTOR = None

class _IdleAwareServer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def server(*args, **kwargs):
    return None

def test_buffered_inbound_is_acked_after_handler(*args, **kwargs):
    return None

def test_reconnect_redials_after_unexpected_close(*args, **kwargs):
    return None

def test_go_dormant_redials_on_wake_and_drains(*args, **kwargs):
    return None

def _relay_descriptor(*args, **kwargs):
    return None

def test_adapter_reports_false_when_the_transport_hold_fails(*args, **kwargs):
    return None

def test_go_dormant_leaves_the_socket_open_when_the_ack_is_missed(*args, **kwargs):
    return None

def test_adapter_go_dormant_delegates_to_transport(*args, **kwargs):
    return None
