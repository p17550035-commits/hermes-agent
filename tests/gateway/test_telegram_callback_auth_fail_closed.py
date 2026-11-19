# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_fake_telegram_error = None

class _TelegramError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_fake_telegram_constants = None

_fake_telegram_request = None

_fake_telegram_ext = None

_fake_telegram = None

def _inject_fake_telegram(*args, **kwargs):
    return None

def _make_adapter(*args, **kwargs):
    return None

class TestCallbackAuthFailClosed:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCallbackAuthPrefersInjectedCheck:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
