from aiohttp import web
import db
from utils import url_fetch, short_generator
import json
import time


routes = web.RouteTableDef()

@routes.get('/get')
async def list(request):
    """
    Список всех сокращений url.

    :param request:
    :return:
    """
    id = short_generator()

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.url.select())
        records = await cursor.fetchall()
        urls = [dict(u) for u in records]
        json_data = []
        for result in urls:
            json_data.append(result)
        return web.Response(text=json.dumps(json_data, default=str))
        # return web.json_response(json_data)


@routes.post('/post')
async def new(request):
    """
    Вставка в базу новой записи.

    :param request:
    :return:
    """
    data = await request.json()
    url = url_fetch(data)
    url_short = short_generator()

    date = time.strftime("%Y-%m-%d")
    async with request.app['db'].acquire() as conn:
        await conn.execute("INSERT INTO url  (url_short, url_long, pub_date) VALUES (%s, %s, %s)", url_short, url, date)
        url = "http://{host}:{port}/{path}".format(
            host=request.app['config']['host'],
            port=request.app['config']['port'],
            path=url_short)
        print("url", url)
        return web.Response(text=url)



async def redirect(request):
    """
    Редирект на полную ссылку.

    :param request:
    :return:
    """
    url_short = request.match_info['url_short']
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute("SELECT url_long FROM url WHERE url_short = %s",url_short)
        record = await cursor.fetchone()

    if record:
        return web.HTTPFound(record[0])
    else:
        raise web.HTTPNotFound()
