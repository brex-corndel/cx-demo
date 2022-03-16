import cx_Oracle
from datetime import datetime, date, timedelta

def get_employment_duration(hire_date):
   days_employed = date.today() - hire_date
   return(days_employed.days)

def employees_by_job_id(job_id):

    sql = """SELECT first_name, last_name
         FROM employees
         WHERE job_id = :jid"""
    cursor.execute(sql, jid=job_id)

    print ("Employees by Job ID : " + job_id)
    for row in cursor:
         print(row)
 #   print('Number of rows is', cursor.rowcount)
    return str(cursor.rowcount)

cx_Oracle.init_oracle_client(lib_dir=r"/Users/jeremybrex/Downloads/instantclient_19_8")

# Establish the database connection
connection = cx_Oracle.connect(user="hr", password="Welcome_1", dsn="localhost/XEPDB1")

# Obtain a cursor
cursor = connection.cursor()

# Data for binding
job_id = "ST_MAN"
emp_count = employees_by_job_id(job_id)
print ("Employees count by Job ID : " + emp_count)

# Function to use pytest
hire_date = date(year=2021, month=7, day=29)
days_employed = get_employment_duration(hire_date)
print(f"Daysn Employee has been employed : {days_employed}")