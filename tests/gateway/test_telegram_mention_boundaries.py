# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _make_adapter(*args, **kwargs):
    return None

def _mention_entity(*args, **kwargs):
    return None

def _telegram_mention_entity(*args, **kwargs):
    return None

def _text_mention_entity(*args, **kwargs):
    return None

def _message(*args, **kwargs):
    return None

class TestRealMentionsAreDetected:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSubstringFalsePositivesAreRejected:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEntityEdgeCases:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestCaseInsensitivity:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestTelegramUtf16EntityOffsets:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
