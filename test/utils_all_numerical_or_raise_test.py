from utils import all_numerical_or_raise
from pytest import raises


def test_all_numerical_or_raise():
    try:
        all_numerical_or_raise([1, 2, 3])
        all_numerical_or_raise([1, 2.0, 3])
        all_numerical_or_raise([1.0, 2.0, 3.0])
    except:
        assert False

    with raises(TypeError):
        all_numerical_or_raise(["One", "Two", "Three"])
        all_numerical_or_raise([1, "Two", 3])
        all_numerical_or_raise([{}, 2, 3])
