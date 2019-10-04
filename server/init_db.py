from sqlalchemy import create_engine, MetaData

from shortener.settings import config
from shortener.db import url

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[url])

if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
