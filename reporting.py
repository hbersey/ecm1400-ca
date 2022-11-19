import air_pollution as ap
import numpy as np
import typing as t
import pandas as pd


def __mean(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant, N: int, get_i: t.Callable[[pd.Timestamp, pd.Timestamp], int]):
    ms_data = data[monitoring_station]

    sigma_n = np.zeros((N, 2))
    dt0 = ms_data.iloc[0]["dt"]
    for _, row in ms_data.iterrows():
        if row[pollutant] == ap.NO_DATA:
            continue

        i = get_i(dt0, row["dt"])
        sigma_n[i][0] += row[pollutant]
        sigma_n[i][1] += 1

    res = np.zeros(N)
    for i in range(N):
        sigma, n = sigma_n[i]
        if n == 0.0:  # Should only happen in testing hopefully
            continue

        res[i] = sigma / n

    return res


def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    return __mean(data, monitoring_station, pollutant, 365, lambda dt0, dt: (dt - dt0) // pd.Timedelta(1, 'D'))


def daily_median(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ms_data = data[ap.monitoring_station_index(monitoring_station)]
    ms_data = ap.select_pollutant(ms_data, pollutant)

    days = [[] for _ in range(365)]
    dt0 = ms_data.iloc[0]["dt"]

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
    return __mean(data, monitoring_station, pollutant, 24, lambda _, dt: dt.hour)


def monthly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    return __mean(data, monitoring_station, pollutant, 12, lambda _, dt: dt.month - 1)


def peak_hour_date(data, date, monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


def count_missing_data(data,  monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


def fill_missing_data(data, new_value,  monitoring_station, pollutant):
    """Your documentation goes here"""

    # Your code goes here
