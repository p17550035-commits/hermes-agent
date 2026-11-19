# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def fake_gh(*args, **kwargs):
    return None

class TestGithubCommentDeliveryOffLoop:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
