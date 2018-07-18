# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from app.blueprints import offers_bp
import settings


def get_app():
    app = Sanic(__name__)

    Initialize(
        app,
        secret=settings.SECRET,
        cookie_set=True,
        cookie_strict=False,
        auth_mode=False)

    app.config.update(dict(LOGO=settings.LOGO))

    app.blueprint(offers_bp)

    return app



