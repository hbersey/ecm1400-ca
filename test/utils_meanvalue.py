from utils import meanvalue
from pytest import raises


def test_meanvalue():
    assert meanvalue([1, 2, 3]) == 2
    assert meanvalue([0.2, 1.0, 2, 3.5]) == 3.35
    with raises(TypeError):
        meanvalue(["Hello, World", 1, 2, 3])
        meanvalue([False, 1, 2, 3])
