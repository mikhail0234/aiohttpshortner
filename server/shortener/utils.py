from aiohttp import web
import random


def url_fetch(data):
    print(data)
    try:
        data = data['url']
    except t.DataError:
        raise web.HTTPBadRequest('URL is not valid')
    return data

def short_generator(size=6, ):
    chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return ''.join(random.choice(chars) for _ in range(size))
