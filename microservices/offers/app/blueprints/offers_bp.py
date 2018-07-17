# -*- coding: utf-8 -*-

from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient
from passlib.hash import pbkdf2_sha256
from sanic import Blueprint, response
from sanic.exceptions import abort
from sanic_jwt import exceptions, protected

import settings
from app.utils import is_valid_uuid


offers_bp = Blueprint('offers', url_prefix='/offer')


@offers_bp.listener('before_server_start')
async def setup_connection(app, loop):
    global db
    motor_uri = settings.DATABASE_URI
    client = AsyncIOMotorClient(motor_uri, io_loop=loop)
    db = client.test_db


