# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _descriptor(*args, **kwargs):
    return None

class FakeTransport:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _adapter(*args, **kwargs):
    return None

class TestDescriptorBit:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFormatHintsStamping:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestMultiPlatformResolution:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
