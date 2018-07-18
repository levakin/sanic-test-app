# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from config import Config
from app.blueprints import user_bp, auth


def get_app():
    app = Sanic(__name__)

    Initialize(
        app,
        authenticate=auth,
        url_prefix='/user/auth',
        secret=Config.SECRET,
        expiration_delta=60 * 60 * 24,
        cookie_set=True,
        cookie_strict=False,
        auth_mode=True)

    app.config.update(dict(LOGO=Config.LOGO))

    app.blueprint(user_bp)

    return app



