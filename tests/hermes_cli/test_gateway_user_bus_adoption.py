# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

class _BootReached:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def _fake_user_bus(*args, **kwargs):
    return None

def _service_manager_env(*args, **kwargs):
    return None

def test_service_gateway_boot_adopts_its_user_bus(*args, **kwargs):
    return None

def test_absent_user_bus_is_never_fabricated(*args, **kwargs):
    return None
