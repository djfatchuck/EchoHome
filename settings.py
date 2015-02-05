USER = ''
PASSWORD = ''

MILIGHT_IP = ''
MILIGHT_PORT = ''

try:
    from local_settings import *
except ImportError:
    pass