import os

from sqlalchemy import create_engine

DB_USER_NAME = os.environ.get('DB_USER_NAME')
DB_PASSWORD = os.environ.get('DB_USER_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')

SQLALCHEMY_DATABASE_URL = f"postgresaql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/fast-api-practice"

create_engine = create_engine(SQLALCHEMY_DATABASE_URL)
a