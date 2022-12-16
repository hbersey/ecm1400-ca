import pandas as pd
from air_pollution import NO_DATA_TEXT
from reporting import count_missing_data
import pytest

__DATA = {
    "TEST": pd.DataFrame([
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, NO_DATA_TEXT, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, NO_DATA_TEXT],
        [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, NO_DATA_TEXT],
    ], columns=["dt", "no", "pm10", "pm25"])
}


def test_count_missing_data():
    # Normal Case
    assert count_missing_data(__DATA, "TEST", "no") == 0
    assert count_missing_data(__DATA, "TEST", "pm10") == 1
    assert count_missing_data(__DATA, "TEST", "pm25") == 4

    # Invalid Station + Pollutant
    with pytest.raises(KeyError):
        count_missing_data(__DATA, "ABC", "pm100")

    with pytest.raises(KeyError):
        count_missing_data(__DATA, "TEST", "pm100")
