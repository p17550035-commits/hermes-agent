# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_LOADED_USER = None

_LOGIN = None

class _LoginSocket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _AnonymousSocket:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _real_db(*args, **kwargs):
    return None

def _create_desktop_session(*args, **kwargs):
    return None

def test_desktop_session_row_records_the_logged_in_user(*args, **kwargs):
    return None

def test_anonymous_desktop_session_row_stays_identity_less(*args, **kwargs):
    return None
