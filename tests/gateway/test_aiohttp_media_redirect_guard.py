# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

PUBLIC_HOST = None

WEIXIN_CDN_HOST = None

INTERNAL_BODY = None

class _LoopbackResolver:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _mattermost_fetch(*args, **kwargs):
    return None

def _weixin_fetch(*args, **kwargs):
    return None

def _weixin_cdn_fetch(*args, **kwargs):
    return None

def test_redirect_to_private_address_is_not_followed(*args, **kwargs):
    return None

def test_timeout_total_covers_the_whole_redirect_chain(*args, **kwargs):
    return None

def test_redirect_does_not_forward_session_authorization_to_another_public_host(*args, **kwargs):
    return None

def test_weixin_cdn_media_downloads_when_a_fake_ip_resolver_answers_the_cdn(*args, **kwargs):
    return None

def test_first_url_is_checked_unless_the_caller_vetted_it(*args, **kwargs):
    return None
