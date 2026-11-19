# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

HOME_NOTICE_SENT = None

HOME_NOTICE_MUTED = None

def settle_home_online_notice_debt(*args, **kwargs):
    return None

class GatewayHomeShutdownNoticeMixin:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
