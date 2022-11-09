from air_pollution import monitoring_station_index, NO_DATA, select_pollutant
import numpy as np


def daily_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""

    ms_data = data[monitoring_station_index(monitoring_station)]
    ms_data = select_pollutant(ms_data, pollutant)

    sigma_n = np.zeros((365, 2))
    dt0 = ms_data[0][0]
    for (dt, val) in ms_data:
        dt: np.datetime64

        if val == NO_DATA:
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

    # Your code goes here


def hourly_average(data, monitoring_station, pollutant):
    """Your documentation goes here"""
    # Your code goes here


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
