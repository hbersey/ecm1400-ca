import air_pollution as ap
import numpy as np


def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ms_data = data[ap.monitoring_station_index(monitoring_station)]
    ms_data = ap.select_pollutant(ms_data, pollutant)

    sigma_n = np.zeros((365, 2))
    dt0 = ms_data[0][0]
    for (dt, val) in ms_data:
        dt: np.datetime64

        if val == ap.NO_DATA:
            continue

        i = (dt - dt0) // np.timedelta64(1, 'D')
        sigma_n[i][0] += val
        sigma_n[i][1] += 1

    res = np.zeros(365)
    for i in range(365):
        sigma, n = sigma_n[i]
        if n == 0.0:  # Should only happen in testing hopefully
            continue

        res[i] = sigma / n

    return res


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ms_data = data[ap.monitoring_station_index(monitoring_station)]
    ms_data = ap.select_pollutant(ms_data, pollutant)

    days = [[] for _ in range(365)]
    dt0 = ms_data[0][0]

    for (dt, val) in ms_data:
        dt: np.datetime64

        if val == ap.NO_DATA:
            continue

        i = (dt - dt0) // np.timedelta64(1, 'D')
        days[i].append(val)

    medians = np.zeros(365)
    for i, values in enumerate(days):

        values = np.sort(np.array(values))
        j = len(values) // 2

        if i % 2 == 1:
            medians[i] = values[j]
            print(values)
            print(medians[i], len(values))
            continue

        medians[i] = (values[j - 1] + values[j]) / 2

    return medians

def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ms_data = data[ap.monitoring_station_index(monitoring_station)]
    ms_data = ap.select_pollutant(ms_data, pollutant)

    sigma_n = np.zeros((24, 2))
    for (dt, val) in ms_data:
        dt: np.datetime64

        if val == ap.NO_DATA:
            continue

        hr = dt.astype(object).hour
        sigma_n[hr][0] += val
        sigma_n[hr][1] += 1

    res = np.zeros(24)
    for i in range(24):
        sigma, n = sigma_n[i]
        if n == 0.0:  # Should only happen in testing hopefully
            continue

        res[i] = sigma / n

    return res


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


def count_missing_data(data,  monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


def fill_missing_data(data, new_value,  monitoring_station, pollutant):
    """Your documentation goes here"""

    # Your code goes here
