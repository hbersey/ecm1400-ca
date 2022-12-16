from reporting import daily_median
from air_pollution import NO_DATA
import pandas as pd
from pytest import raises

__DATA = {
    "TEST": pd.DataFrame(
        [
            [pd.Timestamp("2022-11-23T00:00"), 10.0, 10.0, 10.0],
            [pd.Timestamp("2022-11-23T01:00"), 11.0, 11.0, 12.0],
            [pd.Timestamp("2022-11-23T02:00"), 11.0, 12.0, NO_DATA],
            [pd.Timestamp("2022-11-23T03:00"), 12.0, 13.0, NO_DATA],
        ],
        columns=["dt", "no", "pm10", "pm25"]
    )
}


def test_daily_median():
    # Test valid data
    assert daily_median(__DATA, "TEST", "no")[0] == 11.0
    assert daily_median(__DATA, "TEST", "pm10")[0] == 11.5
    assert daily_median(__DATA, "TEST", "pm25")[0] == 11.0

    # Test no data
    assert daily_median(__DATA, "TEST", "no")[1] == NO_DATA

    # Test invalid data
    with raises(KeyError):
        daily_median(__DATA, "TEST", "co")
