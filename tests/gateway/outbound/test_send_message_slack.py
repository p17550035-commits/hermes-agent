# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ensure_slack_mock(*args, **kwargs):
    return None

class _SlackResponse:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _SlackPostContext:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _SlackSession:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _standalone_send(*args, **kwargs):
    return None

def test_standalone_send_stops_on_non_token_error(*args, **kwargs):
    return None

def test_slack_dm_resolution_error_never_echoes_the_proxy_password(*args, **kwargs):
    return None
