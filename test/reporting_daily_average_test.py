from reporting import daily_average
from air_pollution import NO_DATA
import numpy as np
from pytest import raises

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

    # Test invalid monitoring_station
    with raises(KeyError) as ms_not_found:
        daily_average(__DATA, "ABC", "no")

    assert ms_not_found.value.args[0] == "Monitoring station \"ABC\" was not found."
