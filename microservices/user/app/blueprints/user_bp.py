# -*- coding: utf-8 -*-

from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient
from passlib.hash import pbkdf2_sha256
from sanic import Blueprint, response
from sanic.exceptions import abort
from sanic_jwt import exceptions, protected

import settings
from app.utils import is_valid_username, is_valid_password, is_valid_uuid


user_bp = Blueprint('app', url_prefix='/app')


@user_bp.listener('before_server_start')
async def setup_connection(app, loop):
    global db
    motor_uri = settings.DATABASE_URI
    client = AsyncIOMotorClient(motor_uri, io_loop=loop)
    db = client.test_db


@user_bp.post("/registry")
async def register(request):
    username = request.json.get('username')
    password = request.json.get('password')
    created_at = request.json.get('created_at')
    if username is None or password is None or created_at is None:
        abort(400)  # missing arguments
    if not created_at.isdigit():
        abort(400)  # not digit
    if not is_valid_username(username):
        abort(400)  # not valid username
    if not is_valid_password(password):
        abort(400)  # not valid password
    if await db.users.count_documents({'username': username}) is not 0:
        abort(400)  # existing app
    password_hash = pbkdf2_sha256.hash(password)
    created_at = int(created_at)
    user_id = str(uuid4())

    await db.users.insert_one({
        'user_id': user_id,
        'username': username,
        'password': password_hash,
        'created_at': created_at
    })

    return response.json({'user_id': user_id}, status=201)


async def auth(request, *args, **kwargs):
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        raise exceptions.AuthenticationFailed("Missing username or password.")
    if not is_valid_username(username):
        raise exceptions.AuthenticationFailed("Not valid username.")
    if not is_valid_password(password):
        raise exceptions.AuthenticationFailed("Not valid password.")

    user = await db.users.find_one({'username': username})
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")
    is_verified = pbkdf2_sha256.verify(password, user.get('password'))
    if not is_verified:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return dict(user_id=user.get('user_id'), username=user.get('username'))


@user_bp.get("/<user_id>/")
@protected()
async def get_user(request, user_id):
    if not is_valid_uuid(user_id):
        abort(400)
    user = await db.users.find_one({'user_id': user_id})
    if user is None:
        abort(404)
    return response.json({"user_id": user_id,
                          "username": user.get("username"),
                          "created_at": user.get("created_at")}, status=200)

# class User:
#
#     def __init__(self, user_id, username, password, created_at):
#         self.user_id = user_id
#         self.username = username
#         self.password = password
#         self.created_at = created_at
#
#     def __repr__(self):
#         return "User(user_id='{}')".format(self.user_id)
#
#     def to_dict(self):
#         return {"user_id": self.user_id, "username": self.username, "created_at": self.created_at}

