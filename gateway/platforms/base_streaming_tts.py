# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class AudioFormat:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class StreamingTTSHandle:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def streaming_tts_turn_key(*args, **kwargs):
    return None

def streaming_tts_should_skip_whole_file(*args, **kwargs):
    return None
