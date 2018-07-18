# -*- coding: utf-8 -*-

import os
from distutils.util import strtobool


class Config:
    DEBUG = bool(strtobool(os.getenv('DEBUG', "False")))
    DATABASE_URI = os.getenv('DATABASE_URI', '127.0.0.1:27017')
    WORKERS = int(os.getenv('WORKERS', 2))
    LOGO = os.getenv('LOGO', None)
    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', 8000))
    SECRET = os.getenv('SECRET', 'secret')
