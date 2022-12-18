import pandas as pd
import typing as t


NO_DATA_TEXT = "No data"  # Avoids magic string issues

TStation = t.Literal["HRL", "MY1", "NK1"]
TPollutant = t.Literal["no", "pm10", "pm25"]
TData = t.Dict[TStation, pd.DataFrame]


def __ap_dt(date: t.AnyStr, time: t.AnyStr) -> pd.Timestamp:
    """
    Converts a ``date`` and ``time`` string into a pandas Timestamp and sorts out the 24:00:00 issue.

    Parameters
    ----------
    date: str
        Date in the format YYYY-MM-DD
    time: str
        Time in the format HH:MM:SS

    Returns
    -------
    pd.Timestamp
        A pandas Timestamp object with the ``date`` and ``time`` combined.

    See Also
    --------
    ``__ap_float``: Converts a string to a float using this function.
    """

    # sort out time format
    # eg. 24:15:00 becomes 00:15:00
    if time[:2] == "24":
        time = f"00{time[2:]}"

    return pd.Timestamp(f"{date}T{time}")


def __ap_float(s: t.AnyStr) -> t.Union[float, t.Literal[f"{NO_DATA_TEXT}"]]:
    """
    Converts a string to a float, unless it's the ``NO_DATA_TEXT`` string.

    Parameters
    ----------
    s: str
        String to be converted to a float

    Returns
    -------
    float or str
        ``s`` converted to a float, unless it's the ``NO_DATA_TEXT`` string.

    See Also
    --------
    ``NO_DATA_TEXT``: The string that is returned if ``s`` is the ``NO_DATA_TEXT`` string.
    __read_csv: Converts the ``no``, ``pm10`` and ``pm25`` columns to floats, using this function.
    """

    if s == NO_DATA_TEXT:
        return s
    return float(s)

# Not as efficient as it could be, but it's pandas didn't like my pervious solution:
# https://github.com/hbersey/ecm1400-ca/commit/272604370eca72bbc978b7590b8d0d8dda04d89c


def __read_csv(filename: str) -> pd.DataFrame:
    """
    Read an air pollution CSV file and return a pandas DataFrame. 
    The ``date`` and ``time`` columns are combined into a single ``dt`` column, using ``__ap_dt``.
    The ``no``, ``pm10`` and ``pm25`` columns are converted to floats, using ``__ap_float``.

    Parameters
    ----------
    filename: str
        Name of the CSV file to be read. NB: The file must be in the ``data`` directory.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame with the ``date`` and ``time`` columns combined into a single ``dt`` column and the ``no``, ``pm10`` and ``pm25`` columns converted to floats.

    See Also
    --------
    ``__ap_dt``: Converts a ``date`` and ``time`` string into a pandas Timestamp and sorts out the 24:00:00 issue, used by this function.
    ``__ap_float``: Converts a string to a float, unless it's the ``NO_DATA_TEXT`` string, used by this function.
    """
    data_df = pd.read_csv(
        f"data/{filename}", converters={"no": __ap_float, "pm10": __ap_float, "pm25": __ap_float})
    dt_df = data_df.apply(lambda row: __ap_dt(
        row["date"], row["time"]), axis=1)
    return pd.concat([dt_df.rename("dt"), data_df.drop(["date", "time"], axis=1)], axis=1)


def load_data() -> TData:
    """
    Loads the air pollution data from the CSV files and returns a dictionary of pandas DataFrames.

    Returns
    -------
    TData
        A dictionary of pandas DataFrames, with the keys being the station names and the values being the pandas DataFrames.

    See Also
    --------
    ``__read_csv``: Reads a CSV file and returns a pandas DataFrame, used by this function.
    """

    hrl = __read_csv("Pollution-London Harlington.csv")
    my1 = __read_csv("Pollution-London Marylebone Road.csv")
    nk1 = __read_csv("Pollution-London N Kensington.csv")

    return {
        "HRL": hrl,
        "MY1": my1,
        "NK1": nk1
    }


__data = None


def get_data():
    global __data
    if __data is None:
        __data = load_data()
    return __data


def set_data(data: TData):
    global __data
    __data = data
