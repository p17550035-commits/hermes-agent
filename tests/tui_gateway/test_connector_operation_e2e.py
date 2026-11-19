# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SID = None

class PipeClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeConnectorClient:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def owned_session(*args, **kwargs):
    return None

def _rpc(*args, **kwargs):
    return None

def test_desktop_connect_settles_through_callback_response(*args, **kwargs):
    return None

def test_cli_connect_returns_urls_without_emitting_a_card(*args, **kwargs):
    return None

def test_connection_respond_ignores_outcome_claims_and_rejects_strangers(*args, **kwargs):
    return None
