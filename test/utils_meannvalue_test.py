from utils import meannvalue
from pytest import raises


def test_meannvalue():
    assert meannvalue([1, 2, 3]) == 2
    assert meannvalue([0.2, 1.0, 2, 3.5]) == 1.675
    with raises(TypeError):
        meannvalue(["Hello, World", 1, 2, 3])
        meannvalue([False, 1, 2, 3])
