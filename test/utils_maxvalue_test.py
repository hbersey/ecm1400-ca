from utils import maxvalue
from pytest import raises


def test_maxvalue():
    assert maxvalue([1, 2, 3]) == 3
    assert maxvalue([0.2, 1.0, 2, 3.5]) == 3.5
    with raises(TypeError):
        maxvalue(["Hello, World", 1, 2, 3])
        maxvalue([False, 1, 2, 3])
