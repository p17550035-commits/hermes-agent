# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

_IDENTITY_ATTR = None

_PROVENANCE_ATTRS = None

class IdentityUnresolved:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class RoutingIdentity:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def identity_of(*args, **kwargs):
    return None

def clear_identity(*args, **kwargs):
    return None

def transport_profile_of(*args, **kwargs):
    return None

def replace_source(*args, **kwargs):
    return None

def _name(*args, **kwargs):
    return None

def canonical_identity(*args, **kwargs):
    return None

def restore_identity(*args, **kwargs):
    return None

def resolve_identity(*args, **kwargs):
    return None

AUTH_SUBJECT_PREFIX = None

def parse_authenticated_subject(*args, **kwargs):
    return None

def authenticated_subject(*args, **kwargs):
    return None

def is_authenticated_identity(*args, **kwargs):
    return None

def authenticated_principal_digest(*args, **kwargs):
    return None
