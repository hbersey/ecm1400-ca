import pandas as pd
from air_pollution import NO_DATA_TEXT
from reporting import fill_missing_data

__DATA = {
    "TEST": pd.DataFrame([
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 4.3, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, NO_DATA_TEXT, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, NO_DATA_TEXT],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_fill_missing_data():
    d = fill_missing_data(__DATA, 12.3, "TEST", "pm10")

    assert __DATA["TEST"].iloc[1, 2] == NO_DATA_TEXT
    assert d["TEST"].iloc[0, 2] == 4.3
    assert d["TEST"].iloc[1, 2] == 12.3
