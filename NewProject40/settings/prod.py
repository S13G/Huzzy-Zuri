import os
from .common import *
from django.utils.encoding import force_str as force_text
from urllib.parse import quote as urlquote

ALLOWED_HOSTS = ['studebt4.herokuapp.com']

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

