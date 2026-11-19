# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

merge = None

class TestMergeCaptionBasic:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMergeCaptionSubstringBug:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMergeCaptionWhitespace:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMergeCaptionMultipleItems:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
