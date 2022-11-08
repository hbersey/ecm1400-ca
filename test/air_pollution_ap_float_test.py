from air_pollution import __ap_float, NO_DATA


def test___ap_float():
    assert __ap_float("1.123") == 1.123
    assert __ap_float("-1") == -1.0
    assert __ap_float("No data") == NO_DATA
