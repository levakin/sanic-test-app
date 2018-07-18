# -*- coding: utf-8 -*-

from uuid import uuid4
from time import time

from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Blueprint, response
from sanic.exceptions import abort
from sanic_jwt import exceptions, protected

from config import Config
from app.utils import is_valid_username, is_valid_hash, is_valid_uuid

user_bp = Blueprint('users', url_prefix='/user')


@user_bp.listener('before_server_start')
async def setup_connection(app, loop):
    global db
    motor_uri = Config.DATABASE_URI
    client = AsyncIOMotorClient(motor_uri, io_loop=loop)
    db = client.test_db


@user_bp.post("/registry")
async def register(request):
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        abort(400)  # missing arguments

    try:
        username = str(username)
        password = str(password)
    except ValueError:
        abort(400)

    if not is_valid_username(username):
        abort(400)  # not valid username
    if not is_valid_hash(password):
        abort(400)  # not valid hash

    if await db.users.count_documents({'username': username}) is not 0:
        abort(400)  # existing username

    user_id = str(uuid4())
    created_at = int(time())

    await db.users.insert_one({
        'user_id': user_id,
        'username': username,
        'password': password,
        'created_at': created_at,
        'offers_ids': []})

    return response.json({'user_id': user_id}, status=201)


async def auth(request, *args, **kwargs):
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        raise exceptions.AuthenticationFailed("Missing username or password.")

    try:
        username = str(username)
        password = str(password)
    except ValueError:
        abort(400)

    if not is_valid_username(username):
        raise exceptions.AuthenticationFailed("Not valid username.")
    if not is_valid_hash(password):
        raise exceptions.AuthenticationFailed("Not valid password.")

    user = await db.users.find_one({'username': username})
    if user is None:
        raise exceptions.AuthenticationFailed("User not found.")
    is_correct = password == user.get('password')
    if not is_correct:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return dict(user_id=user.get('user_id'), username=user.get('username'))


@user_bp.get("/<user_id>/")
@protected()
async def get_user(request, user_id):
    try:
        user_id = str(user_id)
    except ValueError:
        abort(400)

    if not is_valid_uuid(user_id):
        abort(400)  # not valid uuid
    user = await db.users.find_one({'user_id': user_id})
    if user is None:
        abort(404)  # user not found

    return response.json({"user_id": user_id,
                          "username": user.get("username"),
                          "created_at": user.get("created_at"),
                          "offers": user.get("offers", [])}, status=200)
