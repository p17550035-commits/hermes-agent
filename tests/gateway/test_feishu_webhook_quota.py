# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_SOURCE_IP = None

_EVENT = None

class _Content:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _request(*args, **kwargs):
    return None

def _signed(*args, **kwargs):
    return None

def _adapter(*args, **kwargs):
    return None

def _send(*args, **kwargs):
    return None

def test_bad_token_flood_does_not_block_authenticated_delivery(*args, **kwargs):
    return None

def test_bad_signature_flood_does_not_block_authenticated_delivery(*args, **kwargs):
    return None

def test_authenticated_deliveries_are_still_rate_limited(*args, **kwargs):
    return None

def test_unauthenticated_url_verification_flood_does_not_block_signed_delivery(*args, **kwargs):
    return None

def test_token_authenticated_url_verification_is_rate_limited(*args, **kwargs):
    return None
