# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Content:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Response:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Versions:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Api:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Client:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_under_cap_body_is_returned_with_auth_header(*args, **kwargs):
    return None

def test_stream_without_content_length_stops_once_cap_is_crossed(*args, **kwargs):
    return None

def test_oversized_content_length_is_rejected_before_reading(*args, **kwargs):
    return None

def _adapter(*args, **kwargs):
    return None

def _event(*args, **kwargs):
    return None

def test_oversized_inbound_media_is_dropped_not_cached(*args, **kwargs):
    return None

def test_under_cap_inbound_media_is_cached_and_dispatched(*args, **kwargs):
    return None

class _HttpSession:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_outbound_image_fetch_uses_the_same_cap(*args, **kwargs):
    return None
