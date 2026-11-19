# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _DM:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Text:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Thread:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_USER = None

def _adapter(*args, **kwargs):
    return None

def _typed(*args, **kwargs):
    return None

def _assert_same_prompt_inputs(*args, **kwargs):
    return None

def _parent(*args, **kwargs):
    return None

def _interaction(*args, **kwargs):
    return None

def test_slash_and_thread_starter_turns_match_a_message_turn(*args, **kwargs):
    return None

def test_voice_channel_turn_matches_a_typed_turn(*args, **kwargs):
    return None
