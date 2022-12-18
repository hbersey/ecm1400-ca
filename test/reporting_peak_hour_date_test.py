import pandas as pd
import air_pollution as ap
from reporting import peak_hour_date

__DATA = {
    "TEST": pd.DataFrame([
        [pd.Timestamp("2020-01-01 00:00:00"), 1.0, 2.0, 3.0],
        [pd.Timestamp("2020-01-01 01:00:00"), 1.0, ap.NO_DATA_TEXT, 3.0],
        [pd.Timestamp("2020-01-01 03:00:00"), 5.0, ap.NO_DATA_TEXT, 3.0],
        [pd.Timestamp("2020-01-01 04:00:00"), 1.0, ap.NO_DATA_TEXT, 3.0],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_peak_hour_date():
    no = peak_hour_date(__DATA, pd.Timestamp("2020-01-01"), "TEST", "no")
    pm10 = peak_hour_date(__DATA, pd.Timestamp("2020-01-01"), "TEST", "pm10")
    pm25 = peak_hour_date(__DATA, pd.Timestamp("2020-01-01"), "TEST", "pm25")

    assert no[0] == 3
    assert no[1] == 5.0

    assert pm10[0] == 0
    assert pm10[1] == 2.0

    assert pm25[0] == 0
    assert pm25[1] == 3.0
