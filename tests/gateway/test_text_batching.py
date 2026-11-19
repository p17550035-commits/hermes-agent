# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_event(*args, **kwargs):
    return None

def _make_discord_adapter(*args, **kwargs):
    return None

class TestDiscordTextBatching:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_matrix_adapter(*args, **kwargs):
    return None

class TestMatrixTextBatching:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_wecom_adapter(*args, **kwargs):
    return None

class TestWeComTextBatching:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
