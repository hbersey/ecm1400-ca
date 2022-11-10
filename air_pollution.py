import numpy as np
import numpy.typing as npt
import typing as t
import csv


__FILES = [
    "Pollution-London Harlington.csv",
    "Pollution-London N Kensington.csv",
    "Pollution-London Marylebone Road.csv"
]

NO_DATA = -1.0
__NO_DATA_TEXT = "No data"  # Avoids magic string issues

# APData = npt.ArrayLike[]


def __ap_dt(date: t.AnyStr, time: t.AnyStr):
    # sort out time format
    # eg. 24:15:00 becomes 00:15:00
    if time[:2] == "24":
        time = f"00{time[2:]}"

    return np.datetime64(f"{date}T{time}")


def __ap_float(s: t.AnyStr):
    if s == __NO_DATA_TEXT:
        return NO_DATA
    return float(s)


def __parse_data(f: t.TextIO):
    data = []
    r = csv.reader(f)
    next(r)  # skip header row

    for (date_s, time_s, no_s, pm10_s, pm25_s) in r:
        dt = __ap_dt(date_s, time_s)
        no = __ap_float(no_s)
        pm10 = __ap_float(pm10_s)
        pm25 = __ap_float(pm25_s)
        data.append([dt, no, pm10, pm25])

    return data


def load_data():
    all_data = []
    for filename in __FILES:
        path = f"data/{filename}"
        f = open(path, "r")
        all_data.append(__parse_data(f))
        f.close()

    # convert to np array at the end because we don't know the number of rows
    # (np arrays not opptimised for dynamic-array-like behaviour)
    return np.array(all_data)


__MONITORING_STATIONS = {
    "HARLINGTON": 0,
    "HRL": 0,
    "N KENSINGTON": 1,
    "NK1": 1,
    "MARYLEBONE ROAD": 2,
    "MY1": 2
}


def monitoring_station_index(s: t.AnyStr):
    s = s.strip().upper()
    if not s in __MONITORING_STATIONS:
        raise KeyError(f"Monitoring station \"{s}\" was not found.")
    return __MONITORING_STATIONS[s]

__POLUTANT_INDECIES = {
    p: i + 1 for (i, p) in enumerate(["no", "pm10", "pm25"])
}


def select_pollutant(data: npt.ArrayLike, pollutant: t.AnyStr) -> npt.ArrayLike:
    if not pollutant in __POLUTANT_INDECIES:
        raise KeyError()

    i = __POLUTANT_INDECIES[pollutant]
    for j in range(3, 0, -1):
        if j == i:
            continue
        data = np.delete(data, j, 1)

    return data
