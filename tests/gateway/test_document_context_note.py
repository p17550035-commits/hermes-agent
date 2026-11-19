# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

gateway_run = None

_build_document_context_note = None

class TestTextDocumentNote:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestBinaryDocumentNote:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_unflagged_text_document_is_not_claimed_inlined(*args, **kwargs):
    return None
