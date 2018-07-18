# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from app.blueprints import offers_bp
from config import Config


def get_app():
    app = Sanic(__name__)

    Initialize(
        app,
        secret=Config.SECRET,
        cookie_set=True,
        cookie_strict=False,
        auth_mode=False)

    app.config.update(dict(LOGO=Config.LOGO))

    app.blueprint(offers_bp)

    return app



