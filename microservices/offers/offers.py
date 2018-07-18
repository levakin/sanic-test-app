# -*- coding: utf-8 -*-

from app import get_app
from config import Config

if __name__ == "__main__":
    app = get_app()
    print(Config.PORT)
    app.run(host=Config.HOST,
            port=Config.PORT,
            debug=Config.DEBUG,
            workers=Config.WORKERS)

