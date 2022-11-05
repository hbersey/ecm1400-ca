from utils import countvalue
from pytest import raises

def test_countvalue():
    assert countvalue([1, 1, 2, 2, 3, 3, 3], 2) == 2
    assert countvalue([1, "Hello, World", 2, False, 3, 3.0, 3], 3) == 2