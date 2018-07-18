# -*- coding: utf-8 -*-

from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Blueprint, response
from sanic.exceptions import abort
from sanic_jwt import protected

import settings
from app.utils import is_valid_uuid, is_valid_text, is_valid_title

offers_bp = Blueprint('offers', url_prefix='/offer')


@offers_bp.listener('before_server_start')
async def setup_connection(app, loop):
    global db
    motor_uri = settings.DATABASE_URI
    client = AsyncIOMotorClient(motor_uri, io_loop=loop)
    db = client.test_db


@offers_bp.post('/create')
async def create(request):
    try:
        user_id = str(request.json.get('user_id'))
        title = str(request.json.get('title'))
        text = str(request.json.get('text'))
        created_at = int(request.json.get('created_at'))
    except ValueError:
        abort(400)

    if user_id is None or title is None or text is None or created_at is None:
        abort(400)  # missing arguments
    if not is_valid_uuid(user_id):
        abort(400)  # not valid uuid
    if not is_valid_title(title):
        abort(400)  # not valid title
    if not is_valid_text(text):
        abort(400)  # not valid text

    if await db.users.count_documents({'user_id': user_id}) is 0:
        abort(404, message="User not found")

    offer_id = str(uuid4())

    document = await db.users.find_one({'user_id': user_id})
    document['offers'].append(offer_id)
    db.users.replace_one({'user_id': user_id}, document)

    await db.offers.insert_one({
        'offer_id': offer_id,
        'user_id': user_id,
        'title': title,
        'text': text,
        'created_at': created_at
    })

    return response.json({'offer_id': offer_id}, status=201)
