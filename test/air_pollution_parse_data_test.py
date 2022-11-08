from air_pollution import __parse_data, NO_DATA
from io import StringIO
import numpy as np

# returns a fake file for testing purposes
def __test_file():
    return StringIO("""date,time,no,pm10,pm25
2021-01-01,01:00:00,1.1,25.8,22.5
2021-03-02,15:23:12,2.2,No data,19.1
2021-05-03,24:00:00,1.3,23.2,21.0
""")


def test___parse_data():
    f = __test_file()
    data = __parse_data(f)

    assert len(data) == 3
    assert len(data[0]) == 4

    assert data[0][0] == np.datetime64("2021-01-01T01:00:00")
    assert data[2][0] == np.datetime64("2021-05-03T00:00:00")
    
    assert data[1][1] == 2.2
    assert data[1][2] == NO_DATA
    assert data[2][3] == 21.0
