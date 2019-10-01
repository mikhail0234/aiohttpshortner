from views import list, new, redirect
from aiohttp import web

def setup_routes(app):
    app.router.add_routes([
                           web.get('/{url_short}', redirect),
                           web.get('/', list),
                           web.post('/new', new)])

