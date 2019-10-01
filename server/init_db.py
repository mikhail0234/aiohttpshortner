# polls/init_db.py
from sqlalchemy import create_engine, MetaData

from shortener.settings import config
from shortener.db import url


DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[url])


def sample_data(engine):
    conn = engine.connect()
    conn.execute(url.insert(), [
        {'url_long': 'https://www.google.com/search?q=google&oq=googl&aqs=chrome.0.0j69i60l3j69i65l2.2222j1j0&sourceid=chrome&ie=UTF-8',
         'url_short': 'localhost:8080/',
         'pub_date': '2019-10-29 19:17:49.629+02'},
        {
            'url_long': 'https://www.google.com/search?q=google&oq=googl&aqs=chrome.0.0j69i60l3j69i65l2.2222j1j0&sourceid=chrome&ie=UTF-8',
            'url_short': 'https://github.com',
            'pub_date': '2019-10-29 19:17:49.629+02'}
    ])


    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
