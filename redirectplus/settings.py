# flake8: noqa
from settings_shared import *

try:
    from redirectplus.local_settings import *
except ImportError:
    pass
