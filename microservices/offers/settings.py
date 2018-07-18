# -*- coding: utf-8 -*-

from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
DATABASE_URI = config('DATABASE_URI', default='127.0.0.1:27017')
WORKERS = config('WORKERS', default=1, cast=int)
LOGO = config('LOGO')
HOST = config('HOST', default='127.0.0.1', cast=str)
PORT = config('PORT', default='8000', cast=int)
SECRET = config('SECRET', default='secret')
MAX_TITLE_LEN = config('MAX_TITLE_LEN', default='30', cast=int)
MAX_TEXT_LEN = config('MAX_TEXT_LEN', default='80', cast=int)