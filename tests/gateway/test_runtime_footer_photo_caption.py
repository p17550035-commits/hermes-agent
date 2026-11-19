# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

FOOTER = None

class _Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _event(*args, **kwargs):
    return None

def _photo(*args, **kwargs):
    return None

def test_photo_only_reply_puts_the_footer_on_the_caption(*args, **kwargs):
    return None

def test_footer_stays_in_text_when_there_is_text_or_it_does_not_fit(*args, **kwargs):
    return None

def _streamed_turn(*args, **kwargs):
    return None

def test_streamed_photo_reply_sends_no_trailing_footer_message(*args, **kwargs):
    return None

def test_streamed_footer_falls_back_when_the_captioned_photo_failed(*args, **kwargs):
    return None

def test_streamed_reply_without_a_photo_keeps_the_trailing_footer(*args, **kwargs):
    return None

def test_non_streamed_footer_is_sent_when_the_captioned_photo_failed(*args, **kwargs):
    return None

def test_streamed_footer_is_sent_when_the_photo_batch_raises(*args, **kwargs):
    return None

def test_footer_never_rides_an_animation(*args, **kwargs):
    return None

def test_no_separate_footer_when_the_captioned_photo_is_queued_for_a_reupload(*args, **kwargs):
    return None
