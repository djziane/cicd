from src import lib
import pytest


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






