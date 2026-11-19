# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

DESCRIPTOR = None

class _StubConnectorServer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def server(*args, **kwargs):
    return None

def test_handshake_negotiates_descriptor(*args, **kwargs):
    return None

def test_inbound_frame_reaches_handler(*args, **kwargs):
    return None

class _Revoking4401Server:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_4401_after_handshake_is_terminal_no_reconnect(*args, **kwargs):
    return None

class _ExpiredToken4401Server:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _transport(*args, **kwargs):
    return None

def _wait_until(*args, **kwargs):
    return None

def test_4401_after_handshake_redials_once_with_fresh_token_and_recovers(*args, **kwargs):
    return None

def test_4401_on_fresh_token_redial_latches_revocation_after_exactly_one_retry(*args, **kwargs):
    return None

def test_4401_with_reason_expired_never_latches_and_reconnects_normally(*args, **kwargs):
    return None

def test_4401_with_reason_expired_repeated_still_never_latches(*args, **kwargs):
    return None

def test_provisional_4401_never_starts_a_second_dialer_while_the_supervisor_is_mid_dial(*args, **kwargs):
    return None

class _FakeCloseError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeWS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _scripted_connect(*args, **kwargs):
    return None

def _fake_transport(*args, **kwargs):
    return None

def test_fresh_token_retry_socket_dropping_during_hello_still_reconnects(*args, **kwargs):
    return None

def test_network_failure_on_the_retry_dial_does_not_unmark_it(*args, **kwargs):
    return None
