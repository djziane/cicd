from src import lib
import pytest
import mysql.connector


@pytest.fixture(scope="session")
def db_conn():
    return mysql.connector.connect(user='root', password='root',
                                  host='127.0.0.1',
                                  database='test_db')

def test_conn(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("select num from test_table")
    record = cursor.fetchone()
    assert record[0]==3