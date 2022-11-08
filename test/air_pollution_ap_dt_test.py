from air_pollution import __ap_dt
import numpy as np

def test___ap_dt():
   assert __ap_dt("2021-12-01", "14:24:10") == np.datetime64("2021-12-01T14:24:10")
   assert __ap_dt("2021-12-01", "24:30:00") == np.datetime64("2021-12-01T00:30:00")
