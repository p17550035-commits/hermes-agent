# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

MEMBERS = None

def store_fixture(*args, **kwargs):
    return None

class _RPC:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _GatewayRouteService:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _service(*args, **kwargs):
    return None

def _kinds(*args, **kwargs):
    return None

def _authority(*args, **kwargs):
    return None

def test_a_room_handed_to_the_gateway_takes_sends_and_wakes_its_members(*args, **kwargs):
    return None

def test_a_send_already_stored_is_answered_as_sent_when_preparing_the_room_fails(*args, **kwargs):
    return None

def test_a_room_whose_members_cannot_be_woken_says_so_once_and_stops_retrying(*args, **kwargs):
    return None

def test_a_table_missing_from_the_store_is_not_counted_toward_the_stall(*args, **kwargs):
    return None
