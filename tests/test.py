from src import lib


def test_metric():
    assert lib.metric() == 1.0


def test_add():
    assert lib.add(1, 2) == 3

