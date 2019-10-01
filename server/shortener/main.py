from aiohttp import web
from db import close_pg, init_pg
from routes import setup_routes
from settings import config

import aiohttp_cors

def main():

    app = web.Application()
    app['config'] = config
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)
    setup_routes(app)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_methods="*",
            allow_headers="*",
            max_age=3600
            )
    })
    for route in app.router.routes():
        cors.add(route)

    web.run_app(app)
if __name__ == "__main__":
    main()
