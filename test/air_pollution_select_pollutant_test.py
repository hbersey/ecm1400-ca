from air_pollution import select_pollutant
import numpy as np
from pytest import raises

__DATA = np.arange(12).reshape((3, 4))


def test_select_pollutant():
    assert np.array_equal(select_pollutant(__DATA, "no"), np.array([
        [0, 1],
        [4, 5],
        [8, 9]
    ]))
    assert np.array_equal(select_pollutant(__DATA, "pm10"), np.array([
        [0, 2],
        [4, 6],
        [8, 10]
    ]))
    assert np.array_equal(select_pollutant(__DATA, "pm25"), np.array([
        [0, 3],
        [4, 7],
        [8, 11]
    ]))

    with raises(KeyError):
        select_pollutant(__DATA, "Hello, World!")
