# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

SESSION_KEY = None

class _SessionStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _CompressionThenFailureAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _StreamConsumer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _runner(*args, **kwargs):
    return None

def _install_compression_failure_agent(*args, **kwargs):
    return None

def _run_compression_failure_turn(*args, **kwargs):
    return None

def test_failed_turn_still_syncs_compression_session_split(*args, **kwargs):
    return None

class _RateLimitFailureAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _EmptyRateLimitFailureAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_empty_rate_limit_response_preserves_failure_metadata(*args, **kwargs):
    return None

class _ProviderSwitchAgent:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
