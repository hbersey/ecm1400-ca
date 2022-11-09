import numpy as np
import numpy.typing as npt
import typing
import csv


__FILES = [
    "Pollution-London Harlington.csv",
    "Pollution-London N Kensington.csv",
    "Pollution-London Marylebone Road.csv"
]

NO_DATA = -1.0
__NO_DATA_TEXT = "No data"  # Avoids magic string issues

# APData = npt.ArrayLike[]


def __ap_dt(date: typing.AnyStr, time: typing.AnyStr):
    # sort out time format
    # eg. 24:15:00 becomes 00:15:00
    if time[:2] == "24":
        time = f"00{time[2:]}"

    return np.datetime64(f"{date}T{time}")


def __ap_float(s: typing.AnyStr):
    if s == __NO_DATA_TEXT:
        return NO_DATA
    return float(s)


def __parse_data(f: typing.TextIO):
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


def load_ap_data():
    all_data = []
    for filename in __FILES:
        path = f"data/{filename}"
        f = open(path, "r")
        all_data.append(__parse_data(f))
        f.close()

    # convert to np array at the end because we don't know the number of rows
    # (np arrays not opptimised for dynamic-array-like behaviour)
    return np.array(all_data)


def monitoring_station_index(s: typing.AnyStr):
    # Todo: Replace this fn with something better
    s = s.upper()

    if s == "HARLINGTON" or s == "HRL":
        return 0
    elif s == "N KENSINGTON" or s == "NK1":
        return 1
    elif s == "MARYLEBONE ROAD" or s == "MY1":
        return 2
