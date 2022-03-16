from how_long.app import employees_by_job_id, get_employment_duration
from sqlalchemy import create_engine
from datetime import date, timedelta
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

def test_employment_duration():
   hire_date = date.today() - timedelta(days=1)
   days_employed = get_employment_duration(hire_date)

   assert int(days_employed) == 1


