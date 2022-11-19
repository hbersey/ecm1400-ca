from reporting import monthly_average
from air_pollution import NO_DATA
import numpy as np
import pandas as pd

__DATA = {
    "HRL": pd.DataFrame([
        [pd.Timestamp("2022-11-23T00:00"), 10.2, 12.2, 13.2],
        [pd.Timestamp("2022-11-23T00:00"), 4.3, 8.1, 9.3],
        [pd.Timestamp("2022-12-24T00:00"), 9.6, 1.0, NO_DATA],
        [pd.Timestamp("2022-12-24T01:00"), 11.0, 12.4, 9.8],
        [pd.Timestamp("2022-11-24T01:00"), 10.1, NO_DATA, 11.2],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_hourly_average():

    no = np.zeros(12)
    no[10] = 8.2
    no[11] = 10.3

    res = monthly_average(__DATA, "HRL", "no")

    assert np.allclose(res, no)
