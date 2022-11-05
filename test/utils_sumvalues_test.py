from utils import sumvalues
from pytest import raises


def test_sumvalues():
    assert sumvalues([1, 2, 3]) == 6
    assert sumvalues([0.2, 1.0, 2, 3.5]) == 6.7
    with raises(TypeError):
        sumvalues(["Hello, World", 1, 2, 3])
        sumvalues([False, 1, 2, 3])
