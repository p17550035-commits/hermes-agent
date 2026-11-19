# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_telegram_adapter(*args, **kwargs):
    return None

def _tg_group_message(*args, **kwargs):
    return None

def _tg_dm_message(*args, **kwargs):
    return None

class TestTelegramAllowedChats:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_dingtalk_adapter(*args, **kwargs):
    return None

class TestDingTalkAllowedChats:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMattermostAllowedChannels:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMatrixAllowedRooms:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
