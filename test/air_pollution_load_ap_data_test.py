from air_pollution import load_ap_data
import numpy as np


def test_load_ap_data():
    data = load_ap_data()

    assert len(data) == 3
    hrl, nk1, my1 = data

    assert len(hrl) == 8760  # ...Harlington.csv
    assert len(my1[0]) == 4

    assert nk1[0][0] == np.datetime64("2021-01-01T01:00:00")
    assert nk1[0][1] == 1.50558
    assert nk1[0][2] == 35.15
    assert nk1[0][3] == 30.448
