from src import lib
import pytest
import mysql.connector

def test_metric():
    assert lib.metric() == 1.0


def test_add():
    assert lib.add(1, 2) == 3

@pytest.mark.parametrize("test_input,expected", [
    (4,8),
    (8,12)
    ])
def test_sum(test_input,expected):
    assert lib.add(test_input,4)==expected



@pytest.fixture(scope="session")
def db_conn():
    return mysql.connector.connect(user='root', password='pass',
                                  host='127.0.0.1',
                                  database='test_db')

def test_conn(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("select num from test_table")
    record = cursor.fetchone()
    assert record[0]==3


