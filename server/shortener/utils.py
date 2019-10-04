from aiohttp import web
import random

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def url_fetch(data):
    print(data)
    try:
        data = data['url']
    except:
        raise web.HTTPBadRequest('URL is not valid')
    return data

def encode(id, chars=CHARS):
    if id == 0:
        return chars[0]
    arr = []
    base = len(chars)
    while id:
        id, rem = divmod(id, base)
        arr.append(chars[rem])
    arr.reverse()
    return ''.join(arr)


def decode(arr, chars=CHARS):
    print(arr)
    l = len(arr)
    id = 0
    for i in range(l):
        power = l-i-1
        id += 62**power * chars.find(arr[i])
    if id == 0:
        return None
    else:
        return id
