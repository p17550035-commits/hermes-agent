# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

logger = None

DEFAULT_CONNECT_TIMEOUT_S = None

DEFAULT_EXEC_TIMEOUT_S = None

DEFAULT_FORWARD_TIMEOUT_S = None

REMOTE_PROBE_TIMEOUT_S = None

CONTROL_PERSIST_S = None

CONTROL_FORWARD_KEEPALIVE_S = None

SUN_PATH_MAX = None

_CONTROL_CHAR_RE = None

_HOSTNAME_RE = None

_IPV6_RE = None

class SshReachError:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

_REDACTIONS = None

def redact_secrets(*args, **kwargs):
    return None

def _reject(*args, **kwargs):
    return None

def _validate_host(*args, **kwargs):
    return None

def validate_ssh_target(*args, **kwargs):
    return None

def validate_key_path(*args, **kwargs):
    return None

def short_control_dir(*args, **kwargs):
    return None

def default_control_dir(*args, **kwargs):
    return None

def control_socket_path(*args, **kwargs):
    return None

def check_short_control_parent(*args, **kwargs):
    return None

def prepare_control_dir(*args, **kwargs):
    return None

class SshEndpoint:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def base_ssh_options(*args, **kwargs):
    return None

def host_args(*args, **kwargs):
    return None

def build_exec_args(*args, **kwargs):
    return None

def build_control_args(*args, **kwargs):
    return None

def build_master_args(*args, **kwargs):
    return None

def forward_spec(*args, **kwargs):
    return None

def login_shell_quote(*args, **kwargs):
    return None

def with_remote_timeout(*args, **kwargs):
    return None

_HOST_KEY_RE = None

_INTERACTIVE_RE = None

_AUTH_RE = None

_UNREACHABLE_RE = None

def classify_ssh_error(*args, **kwargs):
    return None

def ssh_error_message(*args, **kwargs):
    return None

class SshResult:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

class _SshTimeout:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def run_ssh(*args, **kwargs):
    return None

class SshConnection:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None

def pick_local_port(*args, **kwargs):
    return None

def resolve_ssh_binary(*args, **kwargs):
    return None
