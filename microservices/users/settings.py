# -*- coding: utf-8 -*-

from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_URI = config('DATABASE_URI', default='127.0.0.1:27017')
WORKERS = config('WORKERS', default=1, cast=int)
LOGO = config('LOGO')
HOST = config('HOST', default='127.0.0.1')
PORT = config('PORT', default='8000', cast=int)
SECRET = config('SECRET', default='secret')
