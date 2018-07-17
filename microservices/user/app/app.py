# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from app.blueprints import user_bp, auth
import settings


def get_app():
    app = Sanic(__name__)

    Initialize(
        app,
        authenticate=auth,
        url_prefix='/app/auth',
        secret=settings.SECRET,
        expiration_delta=60 * 60 * 24)

    app.config.update(dict(LOGO=settings.LOGO))

    app.blueprint(user_bp)

    return app



