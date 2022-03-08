from sqlalchemy import create_engine
import pytest

# engine = create_engine('user="hr", password="Welcome_1",dsn="localhost/XEPDB1"')
engine = create_engine('oracle://hr:Welcome_1@server:1521/?sid=XEPDB1')

@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()

