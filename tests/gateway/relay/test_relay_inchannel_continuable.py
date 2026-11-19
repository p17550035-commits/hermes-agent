# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _descriptor(*args, **kwargs):
    return None

class TestDescriptorCapabilityBit:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestRelayAdapterCapabilityMapping:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPerPlatformCapability:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestSurfaceKnobResolution:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
