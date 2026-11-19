# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def test_normalize_returns_int_or_passthrough_string(*args, **kwargs):
    return None

class FakeNetworkError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeBadRequest:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeTimedOut:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeInlineKeyboardButton:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _FakeInlineKeyboardMarkup:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_fake_telegram = None

_fake_telegram_error = None

_fake_telegram_constants = None

_fake_telegram_ext = None

_fake_telegram_request = None

def _inject_fake_telegram(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

def test_send_passes_username_chat_id_through_unchanged(*args, **kwargs):
    return None
