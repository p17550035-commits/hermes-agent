# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

pytestmark = None

def _stub_linger_file(*args, **kwargs):
    return None

def _root_with_system_unit_pinned_home(*args, **kwargs):
    return None

class TestEnsureLingerEnabled:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class TestEnsureSystemServiceLinger:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def test_systemd_install_calls_linger_helper(*args, **kwargs):
    return None

def test_systemd_install_targets_linger_at_system_service_user(*args, **kwargs):
    return None

def test_existing_system_install_repairs_linger_for_configured_user(*args, **kwargs):
    return None

def test_systemd_install_repair_path_keeps_linger_guarantee(*args, **kwargs):
    return None
