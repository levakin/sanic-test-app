# -*- coding: utf-8 -*-

from app import get_app
import settings

if __name__ == "__main__":
    app = get_app()
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG, workers=settings.WORKERS)

