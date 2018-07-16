# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jwt import Initialize

from app.content.user_bp import user_bp
from settings import Config


async def authenticate(request):
    return dict(user_id="some_id")


app = Sanic(__name__)
Initialize(app, authenticate=authenticate)

app.config.update(dict(LOGO=Config.LOGO))
print(Config.DEBUG)
app.blueprint(user_bp)

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG, workers=Config.WORKERS)
