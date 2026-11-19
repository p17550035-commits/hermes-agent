# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PROTOCOL_VERSION = None

MAX_TOKEN_BYTES = None

MAX_PROMPT_BYTES = None

_IDENTIFIER_RE = None

_DIGEST_RE = None

_LINK_MODES = None

LinkMode = None

TransportSecurity = None

class HostedRoomPeerError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class HostedRoomGrantError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_ROOM_GRANT_SECRET_FILE = None

def _gateway_room_grant_secret_for_home(*args, **kwargs):
    return None

def gateway_room_grant_secret(*args, **kwargs):
    return None

def gateway_room_grant_secret_available(*args, **kwargs):
    return None

def derive_room_grant_secret(*args, **kwargs):
    return None

def _identifier(*args, **kwargs):
    return None

def _positive_int(*args, **kwargs):
    return None

def _digest(*args, **kwargs):
    return None

_exact_fields = None

def _canonical_json(*args, **kwargs):
    return None

def _b64encode(*args, **kwargs):
    return None

def _b64decode(*args, **kwargs):
    return None

def _split_token(*args, **kwargs):
    return None

def _non_empty_list(*args, **kwargs):
    return None

def _parse_link_modes(*args, **kwargs):
    return None

def _protocol_versions(*args, **kwargs):
    return None

def _catalog_digest(*args, **kwargs):
    return None

def _parse_endpoint(*args, **kwargs):
    return None

_CATALOG_FIELDS = None

class GatewayRoomCatalog:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def catalog_mapping(*args, **kwargs):
    return None

local_catalog_mapping = None

def local_room_link_endpoint(*args, **kwargs):
    return None

def served_room_link_endpoint(*args, **kwargs):
    return None

def _room_link_url_from_config(*args, **kwargs):
    return None

def _configured_room_link_url(*args, **kwargs):
    return None

def validate_room_link_url(*args, **kwargs):
    return None

class HostedMemberDispatch:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_GRANT_SCOPE = None

_GRANT_FIELDS = None

_GRANT_REFRESH_FIELDS = None

_GRANT_PERMISSIONS = None

MAX_DISPATCH_GRANT_TTL_SECONDS = None

MAX_STATUS_GRANT_TTL_SECONDS = None

def issue_room_grant(*args, **kwargs):
    return None

def verify_room_grant(*args, **kwargs):
    return None

def decode_room_grant(*args, **kwargs):
    return None

def room_grant_hard_expiry(*args, **kwargs):
    return None

def room_grant_matches_scope(*args, **kwargs):
    return None

def room_grant_needs_dispatch_refresh(*args, **kwargs):
    return None
