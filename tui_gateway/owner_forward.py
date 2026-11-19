# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

FORWARDABLE_LEDGER_STATES = None

ADMIT_TIMEOUT_S = None

RELAY_TIMEOUT_S = None

RELAY_FINALIZE_POLL_S = None

_RELAYED = None

_REFUSED_BEFORE_COMMIT = None

class OwnerUnavailable:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class OwnerNotRunning:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class OwnerUnconfirmed:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def discover_owner(*args, **kwargs):
    return None

def connect_owner(*args, **kwargs):
    return None

def forwardable(*args, **kwargs):
    return None

def _payload_for(*args, **kwargs):
    return None

class _Relay:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def forward_rpc(*args, **kwargs):
    return None

def forward_prompt(*args, **kwargs):
    return None
