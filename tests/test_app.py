from how_long.app import employees_by_job_id
from sqlalchemy import create_engine
import pytest

def test_job_id_search(): 
  True

def test_db_conn():

    engine = create_engine('oracle://hr:Welcome_1@server:1521/?sid=XEPDB1')

    @pytest.fixture(scope='module')
    def connection():
      connection = engine.connect()
      yield connection
#    connection.close()

def test_job_id_search(): 

    job_id = "ST_MAN"
    emp_count = employees_by_job_id(job_id)

    assert int(float(emp_count)) > 0

