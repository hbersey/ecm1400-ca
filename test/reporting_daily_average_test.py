from reporting import daily_average
from air_pollution import NO_DATA_TEXT
import numpy as np
from pytest import raises
import pandas as pd

__DATA = {
    "HRL": pd.DataFrame([
        [pd.Timestamp("2022-11-23T00:00"), 10.1, 12.2, 13.2],
        [pd.Timestamp("2022-11-23T09:00"), 11.0, 12.4, 9.8],
        [pd.Timestamp("2022-11-24T23:00"), 10.4, NO_DATA_TEXT, 11.2],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_daily_average():

    # Test no on __DATA with valid args
    no = np.zeros(365)
    no[0] = 10.55
    no[1] = 10.4

    np.array_equal(daily_average(__DATA, "HRL", "no"), no)

    # Test invalid monitoring_station
    with raises(KeyError) as ms_not_found:
        daily_average(__DATA, "ABC", "no")

    assert ms_not_found.value.args[0] == "ABC"
