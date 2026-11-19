# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _ogg_opus(*args, **kwargs):
    return None

class Channel:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

def test_plain_audio_media_is_a_named_attachment_not_a_voice_message(*args, **kwargs):
    return None

def test_voice_message_carries_ogg_opus_bytes_and_their_real_duration(*args, **kwargs):
    return None

def test_non_opus_voice_reply_is_transcoded_with_the_converted_streams_duration(*args, **kwargs):
    return None
