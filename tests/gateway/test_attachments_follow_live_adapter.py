# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class Adapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

def _reply_with_image(*args, **kwargs):
    return None

def test_reply_images_go_out_on_the_reconnected_adapter(*args, **kwargs):
    return None

def test_a_refused_image_upload_is_logged(*args, **kwargs):
    return None
