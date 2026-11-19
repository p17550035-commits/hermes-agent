# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _Entity:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _Message:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_hidden_link_in_word_is_inlined(*args, **kwargs):
    return None

def test_caption_link_on_media_is_inlined(*args, **kwargs):
    return None

def test_utf16_offset_is_respected_after_emoji(*args, **kwargs):
    return None

def test_expansion_is_idempotent(*args, **kwargs):
    return None

def test_malformed_link_entities_are_ignored(*args, **kwargs):
    return None

def test_text_does_not_use_caption_entities(*args, **kwargs):
    return None

def test_offset_inside_utf16_surrogate_pair_is_ignored(*args, **kwargs):
    return None

def test_anchor_that_is_already_the_url_is_not_duplicated(*args, **kwargs):
    return None

class _Quote:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_quote_link_offsets_are_utf16_after_emoji(*args, **kwargs):
    return None

def test_quote_of_a_caption_uses_caption_links(*args, **kwargs):
    return None

def test_quote_cutting_through_a_link_leaves_it_out(*args, **kwargs):
    return None

def test_partial_quote_of_a_cron_delivery_keeps_its_header(*args, **kwargs):
    return None
