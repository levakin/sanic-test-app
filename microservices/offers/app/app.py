# -*- coding: utf-8 -*-

from sanic import Sanic

from app.blueprints import offers_bp, auth
import settings


def get_app():
    app = Sanic(__name__)

    app.config.update(dict(LOGO=settings.LOGO))

    app.blueprint(offers_bp)

    return app



