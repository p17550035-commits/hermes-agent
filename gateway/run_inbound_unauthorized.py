# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_MAX_SENDER_NAME_CHARS = None

_MAX_SEEN_SENDERS = None

logger = None

def pairing_profile_arg(*args, **kwargs):
    return None

def pairing_code_reply(*args, **kwargs):
    return None

def pairing_rate_limited_reply(*args, **kwargs):
    return None

def unauthorized_owner_hint(*args, **kwargs):
    return None

class UnauthorizedOwnerNotifier:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
