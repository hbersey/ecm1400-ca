from reporting import hourly_average
from air_pollution import NO_DATA
import numpy as np
import pandas as pd

__DATA = {
    "HRL": pd.DataFrame([
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 12.2, 13.2],
        [pd.Timestamp("2022-11-23T00:00"), 4.4, 8.1, 9.3],
        [pd.Timestamp("2022-12-24T00:00"), 9.6, 1.0, NO_DATA],
        [pd.Timestamp("2022-12-24T01:00"), 11.0, 12.4, 9.8],
        [pd.Timestamp("2022-11-24T01:00"), 10.4, NO_DATA, 11.2],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_hourly_average():

    no = np.zeros(24)
    no[0] = 8.0
    no[1] = 10.7

    assert np.array_equal(hourly_average(__DATA, "HRL", "no"), no)
