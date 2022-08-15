import os

import dj_database_url

from .common import *
from django.utils.encoding import force_str as force_text
from urllib.parse import quote as urlquote

ALLOWED_HOSTS = ['studebt4.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config()
}

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

