import air_pollution as ap
import numpy as np
import numpy.typing as npt
import typing as t
import pandas as pd


def __mean(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant, N: int, get_i: t.Callable[[pd.Timestamp, pd.Timestamp], int]) -> float:
    """
    Calculate the mean of a pollutant for a monitoring station over a regular interval.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated
    N:
        Size of output array
    get_i: function, takes (pd.Timestamp, pd.Timestamp) and returns int 
        Function to get the index of the output array from the start date and the current date 

    Returns
    -------
    float
    """
    ms_data = data[monitoring_station]

    sigma_n = np.zeros((N, 2))
    dt0 = ms_data.iloc[0]["dt"]
    for _, row in ms_data.iterrows():
        if row[pollutant] == ap.NO_DATA_TEXT:
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


def daily_average(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> npt.NDArray[np.float64]:
    """
    Returns the daily (mean) averages for a given monitoring station and pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    list of float (size 365)
        the daily averages
    """
    return __mean(data, monitoring_station, pollutant, 365, lambda dt0, dt: (dt - dt0) // pd.Timedelta(1, 'D'))


def daily_median(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant):
    """
    Returns the daily medians for a given monitoring station and pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    list of float (size 365)
        the daily medians. Returns zero if there is no data for a day.
    """

    ms_data = data[monitoring_station]

    days = [[] for _ in range(365)]
    dt0 = ms_data.iloc[0]["dt"]

    for _, row in ms_data.iterrows():
        dt: np.datetime64 = row["dt"]
        val: float = row[pollutant]

        if val == ap.NO_DATA_TEXT:
            continue

        i = (dt - dt0) // np.timedelta64(1, 'D')
        days[i].append(val)

    medians = np.zeros((365, 1))
    for i, values in enumerate(days):

        values = np.sort(np.array(values))

        if len(values) == 0:
            # TODO: Research: "Is this the right thing to do. OR should I raise an error?"
            medians[i] = 0
            continue

        j = len(values) // 2

        if i % 2 == 1:
            medians[i] = values[j]
            print(values)
            print(medians[i], len(values))
            continue

        medians[i] = (values[j - 1] + values[j]) / 2

    return medians


def hourly_average(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> npt.NDArray[np.float64]:
    """
    Returns the hourly (mean) averages for a given monitoring station and pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    list of float (size 24)
        the hourly averages
    """
    return __mean(data, monitoring_station, pollutant, 24, lambda _, dt: dt.hour)


def monthly_average(data: ap.TData, monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> npt.NDArray[np.float64]:
    """
    Returns the monthly (mean) averages for a given monitoring station and pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    list of float (size 24)
        the monthly averages
    """
    return __mean(data, monitoring_station, pollutant, 12, lambda _, dt: dt.month - 1)


# Maybe pd.timestamp isn't the best type for this
def peak_hour_date(data: ap.TData, date: pd.Timestamp, monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> int:
    """
    Returns the hour of the given date with the highest level of the given pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    date: pd.Timestamp
        The date to check
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    int
        The hour of the day with the highest level of the given pollutant
    """

    day = data[monitoring_station][data[monitoring_station]
                                   ["dt"].dt.date == date.date()]

    hr = -1
    max_ = -1.0

    for _, row in day.iterrows():
        val = row[pollutant]

        if val == ap.NO_DATA_TEXT:
            continue
        elif val > max_:
            hr = row["dt"].hour
            max_ = val

    return hr


def count_missing_data(data: ap.TData,  monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> int:
    """
    Returns the number of missing data points for a given monitoring station and pollutant.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    int
        The number of missing data points

    """

    values = data[monitoring_station][pollutant]

    n = 0
    for item in values:
        if item == ap.NO_DATA_TEXT:
            n += 1

    return n


# Not sure what type is best of new_value
def fill_missing_data(data: ap.TData, new_value: t.Any,  monitoring_station: ap.TStation, pollutant: ap.TPollutant) -> ap.TData:
    """
    Returns the data with the missing data points filled with the given value.

    Parameters
    ----------
    data: ap.TData
        All monitoring station data
    new_value: any (preferably float)
        The value to fill the missing data points with
    monitoring_station: ap.TStation
        The monitoring station being used
    pollutant: ap.TPollutant
        The pollutant being calculated

    Returns
    -------
    ap.TData
        The data with the missing data points filled with the given value
    """

    updated_df = data[monitoring_station].copy()
    for i, row in updated_df.iterrows():
        if row[pollutant] == ap.NO_DATA_TEXT:
            updated_df.at[i, pollutant] = new_value

    new_data = {
        **data,
        monitoring_station: updated_df
    }

    return new_data
