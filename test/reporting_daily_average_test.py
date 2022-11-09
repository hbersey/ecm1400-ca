from reporting import daily_average
from air_pollution import NO_DATA
import numpy as np

__DATA = np.array([
    [
        [np.datetime64("2022-11-23T00:00"), 10.1, 12.2, 13.2],
        [np.datetime64("2022-11-23T09:00"), 11.0, 12.4, 9.8],
        [np.datetime64("2022-11-24T23:00"), 10.4, NO_DATA, 11.2],
    ]
])


def test_daily_average():

    # Test no on __DATA with valid args
    no = np.zeros(365)
    no[0] = 10.55
    no[1] = 10.4

    np.array_equal(daily_average(__DATA, "HRL", "no"), no)

    # assert daily_average(__DATA, "HRL", "pm10") == 12.3
    # assert daily_average(__DATA, "HRL", "pm25") == 11.4

    # TODO: Add tests for throwing exceptions
