# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from app.content.user_bp import user_bp, auth
from settings import Config

app = Sanic(__name__)

sanicjwt = Initialize(
    app,
    authenticate=auth,
    url_prefix='/user/auth',
    secret=Config.SECRET)

app.config.update(dict(LOGO=Config.LOGO))

app.blueprint(user_bp)

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG, workers=Config.WORKERS)
