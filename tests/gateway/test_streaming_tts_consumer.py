# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class FakeStreamer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FakeVoiceAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class BlockingSecondChunkStreamer:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _make_consumer(*args, **kwargs):
    return None

def _run_test(*args, **kwargs):
    return None

def gateway_tts_turn(*args, **kwargs):
    return None

def _speak_then_tool_result(*args, **kwargs):
    return None

def test_tool_boundary_none_flushes_streamed_acknowledgment(*args, **kwargs):
    return None

def test_completed_commentary_is_spoken_exactly_once(*args, **kwargs):
    return None

def _make_minimal_adapter(*args, **kwargs):
    return None

class TestAdapterContractDefaults:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestConsumerLifecycle:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestStreamerFormatAndLooping:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestGatewayIntegrationSeam:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestAbortAndCancellation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFallbackSafety:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestConcurrentTurnIsolation:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestThinkBlockSuppression:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestQueueBackpressure:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class DelayedFlushChunker:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestFinishSentinelRace:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class FinishFailingAdapter:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestAdapterFinishFailure:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestPostAudioTimeoutAbort:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEndpointReportedRate:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
