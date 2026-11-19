# NEUTRALIZED BY NUKE_BLOAT: 0ms local no-op stub

_PACKAGE_SCHEMA_VERSION = None

_STORE_SCHEMA_VERSION = None

_BUSY_TIMEOUT_MS = None

_SCHEMA_BUSY_TIMEOUT_MS = None

_DEFERRED_WRITES_MAX = None

_LOCAL_HISTORY_RETENTION_DAYS = None

_ACTIVE_INSTALL_STATE_KEY = None

_INSTALL_SNAPSHOT_STATE_KEY = None

_MILESTONE_STATE_PREFIX = None

_FEATURE_STATE_PREFIX = None

_DAILY_ONCE_STATE_PREFIX = None

_ACTIVE_INSTALL_INTERVAL = None

_RESOURCE_COLUMNS = None

_CREATE_TELEMETRY_STATE_SQL = None

_CREATE_COUNTER_AGGREGATES_SQL = None

_CREATE_PACKAGE_OUTBOX_SQL = None

_CREATE_CONSENT_TABLES_SQL = None

_MIGRATE_V1_SQL = None

_PENDING_PERIOD_COUNT_SQL = None

_INCREMENT_COUNTER_SQL = None

_SEND_COLUMNS = None

logger = None

_DEFERRING_STORES_LOCK = None

def drain_deferring_stores(*args, **kwargs):
    return None

def _utc_now(*args, **kwargs):
    return None

def _isoformat(*args, **kwargs):
    return None

def _compact_json(*args, **kwargs):
    return None

def _row_resource(*args, **kwargs):
    return None

def _ensure_private(*args, **kwargs):
    return None

class SharedMetricsStore:
    def __init__(self, *args, **kwargs): pass
    def __getattr__(self, name): return lambda *a, **kw: None
