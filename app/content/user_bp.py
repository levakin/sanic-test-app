from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Blueprint
from sanic import response
from sanic.exceptions import abort

from settings import Config
from ..utils import is_valid_username, is_valid_password, is_valid_uuid

user_bp = Blueprint('user', url_prefix='/user')


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
        abort(400)  # existing user
    created_at = int(created_at)
    user_id = str(uuid4())

    await db.users.insert_one({
        'user_id': user_id,
        'username': username,
        'password': password,
        'created_at': created_at
    })

    return response.text('OK', status=201)


@user_bp.post("/auth")
async def auth(request):
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)  # missing arguments
    if not is_valid_username(username):
        abort(400)  # not valid username
    if not is_valid_password(password):
        abort(400)  # not valid password

    user = await db.users.find_one({'username': username, 'password': password})
    return response.json({'id': user.get('user_id')}, status=200)


@user_bp.get("/<user_id>/")
async def get_user(request, user_id):
    if not is_valid_uuid(user_id):
        abort(400)
    user = await db.users.find_one({'user_id': user_id})
    return response.json({"user_id": user_id,
                          "username": user.get("username"),
                          "created_at": user.get("created_at")}, status=200)
