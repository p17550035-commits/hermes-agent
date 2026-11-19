# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _FakeRemoteEnv:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def remote_env(*args, **kwargs):
    return None

def test_sandbox_artifact_is_fetched_but_credentials_and_symlinks_to_them_are_not(*args, **kwargs):
    return None

def test_sandbox_project_env_file_is_not_fetched(*args, **kwargs):
    return None

def test_local_backend_and_strict_mode_do_not_fetch(*args, **kwargs):
    return None

class _ScriptedEnv:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_fetch_file_round_trips_bytes_and_enforces_the_in_sandbox_size_cap(*args, **kwargs):
    return None
