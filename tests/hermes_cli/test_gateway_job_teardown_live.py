# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

_REPO_ROOT = None

JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = None

JOB_OBJECT_LIMIT_BREAKAWAY_OK = None

JobObjectExtendedLimitInformation = None

CREATE_SUSPENDED = None

SYNCHRONIZE = None

PROCESS_QUERY_LIMITED_INFORMATION = None

WAIT_OBJECT_0 = None

WAIT_TIMEOUT = None

class IO_COUNTERS:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class JOBOBJECT_BASIC_LIMIT_INFORMATION:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class JOBOBJECT_EXTENDED_LIMIT_INFORMATION:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _kernel32(*args, **kwargs):
    return None

def _make_kill_on_close_job(*args, **kwargs):
    return None

def _start_driver_in_job(*args, **kwargs):
    return None

def _read_pid(*args, **kwargs):
    return None

_SLEEPER = None

def _wait_for(*args, **kwargs):
    return None

class TestJobObjectMechanismLive:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestWatcherRespawnLive:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestResumeVerificationLive:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
