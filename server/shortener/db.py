import aiopg.sa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

url = Table(
    'url', meta,

    Column('id', Integer, primary_key=True),
    Column('url_long', String(200), nullable=False),
    Column('url_short', String(200), nullable=False),
    Column('pub_date', Date, nullable=False),
    Column('exp_date', Date, nullable=False)
)

async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine

async def insert_url(app):

    conn = app['db'].connect()

    await conn.execute(url.insert(), [
        {
            'url_long': 'https://www.google.com/search?q=google&oq=googl&aqs=chrome.0.0j69i60l3j69i65l2.2222j1j0&sourceid=chrome&ie=UTF-8',
            'url_short': 'localhost:8080/',
            'pub_date': '2019-10-30 19:17:49.629+02'},
        {
            'url_long': 'https://www.google.com/search?q=google&oq=googl&aqs=chrome.0.0j69i60l3j69i65l2.2222j1j0&sourceid=chrome&ie=UTF-8',
            'url_short': 'https://github.com',
            'pub_date': '2019-10-30 19:17:49.629+02'}
    ])


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()

async def get_url(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine
