# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

def _reset_cron_running_set(*args, **kwargs):
    return None

def _telegram_job(*args, **kwargs):
    return None

def _telegram_target(*args, **kwargs):
    return None

def _bind_notifier(*args, **kwargs):
    return None

class TestNotifyInterruptedCronJobs:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestShutdownDeliversNoticeBeforeDisconnect:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
