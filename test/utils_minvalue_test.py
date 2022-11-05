from utils import minvalue
from pytest import raises


def test_minvalue():
    assert minvalue([1, 2, 3]) == 1
    assert minvalue([0.2, 1.0, 2, 3.5]) == 0.2
    with raises(TypeError):
        minvalue(["Hello, World", 1, 2, 3])
        minvalue([False, 1, 2, 3])
