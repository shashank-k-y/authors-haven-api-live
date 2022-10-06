from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default='o9l%zzooi3n0m$!jis^1q6a@30=2bpt_hy5arv3njk*@u48a@v',
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]