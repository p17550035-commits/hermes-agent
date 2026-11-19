# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class SessionAuthorities:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class LocalBot:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def local_bots(*args, **kwargs):
    return None

def served_profile_name(*args, **kwargs):
    return None

def authority_for_home(*args, **kwargs):
    return None

def authority_for_profile_id(*args, **kwargs):
    return None

def active_authority(*args, **kwargs):
    return None

def require_active_authority(*args, **kwargs):
    return None

def all_authorities(*args, **kwargs):
    return None

def serving_authorities(*args, **kwargs):
    return None

def require_serving(*args, **kwargs):
    return None

def admission_owner(*args, **kwargs):
    return None

def holds_admission(*args, **kwargs):
    return None

def _prepare_owner_scope(*args, **kwargs):
    return None

def async_owner_scope(*args, **kwargs):
    return None

def owner_scope(*args, **kwargs):
    return None
