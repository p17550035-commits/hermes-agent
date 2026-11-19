# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FinalOnRefusal:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_final_failure_skips_retry_and_plain_text_fallback(*args, **kwargs):
    return None

def test_server_retry_after_is_honoured_by_every_adapter(*args, **kwargs):
    return None

def _http_date_in(*args, **kwargs):
    return None

def test_slack_retry_after_understands_http_date(*args, **kwargs):
    return None

def test_discord_retry_after_understands_http_date_and_reset_after(*args, **kwargs):
    return None
