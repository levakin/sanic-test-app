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
    user_id = request.json.get('user_id')
    title = request.json.get('title')
    text = request.json.get('text')
    created_at = request.json.get('created_at')

    if user_id is None or title is None or text is None or created_at is None:
        abort(400)  # missing arguments

    try:
        user_id = str(user_id)
        title = str(title)
        text = str(text)
        created_at = int(created_at)
    except ValueError:
        abort(400)

    if not is_valid_uuid(user_id):
        abort(400)  # not valid uuid
    if not is_valid_title(title):
        abort(400)  # not valid title
    if not is_valid_text(text):
        abort(400)  # not valid text

    if await db.users.count_documents({'user_id': user_id}) is 0:
        abort(404, message="User not found")

    offer_id = str(uuid4())

    user = await db.users.find_one({'user_id': user_id})
    user['offers'].append(offer_id)
    db.users.replace_one({'user_id': user_id}, user)

    await db.offers.insert_one({
        'offer_id': offer_id,
        'user_id': user_id,
        'title': title,
        'text': text,
        'created_at': created_at
    })

    return response.json({'offer_id': offer_id}, status=201)


@offers_bp.post('/')
async def get_offers(request):
    user_id = request.json.get('user_id')
    offer_id = request.json.get('offer_id')

    if user_id is None and offer_id is None:
        abort(400)  # missing arguments

    if offer_id:
        offer = await db.offers.find_one({'offer_id': offer_id})

        return response.json({"offer_id": offer.get("offer_id"),
                              "user_id": offer.get("user_id"),
                              "title": offer.get("title"),
                              "text": offer.get("text"),
                              "created_at": offer.get("created_at")})
    else:
        user = await db.users.find_one({'user_id': user_id})
        offers = []
        offers_ids = user['offers']
        for offer_id in offers_ids:
            offer = await db.offers.find_one({'offer_id': offer_id})
            offer_dump = {"offer_id": offer.get("offer_id"),
                          "user_id": offer.get("user_id"),
                          "title": offer.get("title"),
                          "text": offer.get("text"),
                          "created_at": offer.get("created_at")}
            offers.append(offer_dump)
        return response.json({"offers": offers})
