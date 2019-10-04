from aiohttp import web
import db
from utils import url_fetch, encode, decode
import json
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime


routes = web.RouteTableDef()

@routes.get('/get')
async def list(request):
    """
    Список всех сокращений url.

    :param request:
    :return:
    """

    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.url.select())
        records = await cursor.fetchall()
        urls = [dict(u) for u in records]
        json_data = []
        for result in urls:
            json_data.append(result)
        return web.Response(text=json.dumps(json_data, default=str))


@routes.post('/post')
async def new(request):
    """
    Вставка в базу новой записи.

    :param request:
    :return:
    """
    data = await request.json()
    url = url_fetch(data)


    date = time.strftime("%Y-%m-%d")
    exp_date = datetime.today()+ relativedelta(months=6)
    exp_date = exp_date.strftime("%Y-%m-%d")
    print(exp_date)
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute("INSERT INTO url  (url_long, url_short, pub_date, exp_date) VALUES (%s, %s, %s, %s) RETURNING id;",

                              url, "", date, exp_date)

        id = await cursor.fetchall()
        print("ID ", type(id[0][0]))
        url_short = encode(id[0][0])

        print("url_short ", url_short)

        await conn.execute("UPDATE url  SET url_short = %s WHERE id= %s", url_short, id[0][0])
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
    id = decode(url_short)
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute("SELECT url_long FROM url WHERE id = %s",id)
        record = await cursor.fetchone()
    print(record)
    if record:
        return web.HTTPFound(record[0])
    else:
        raise web.HTTPNotFound()
