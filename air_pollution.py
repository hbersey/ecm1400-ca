import pandas as pd
import typing as t


NO_DATA = -1.0
__NO_DATA_TEXT = "No data"  # Avoids magic string issues

TStation = t.Literal["HRL", "MY1", "NK1"]
TPollutant = t.Literal["no", "pm10", "pm25"]
TData = t.Dict[TStation, pd.DataFrame]


def __ap_dt(date: t.AnyStr, time: t.AnyStr):
    # sort out time format
    # eg. 24:15:00 becomes 00:15:00
    if time[:2] == "24":
        time = f"00{time[2:]}"

    return pd.Timestamp(f"{date}T{time}")


def __ap_float(s: t.AnyStr):
    if s == __NO_DATA_TEXT:
        return NO_DATA
    return float(s)


def __read_csv(filename):
    return pd.read_csv(f"data/{filename}", parse_dates={"dt": ["date", "time"]}, date_parser=__ap_dt,
                       na_values=__NO_DATA_TEXT, converters={3: __ap_float, 4: __ap_float, 5: __ap_float})


def load_data():
    hrl = __read_csv("Pollution-London Harlington.csv")
    my1 = __read_csv("Pollution-London Marylebone Road.csv")
    nk1 = __read_csv("Pollution-London N Kensington.csv")

    return {
        "HRL": hrl,
        "MY1": my1,
        "NK1": nk1
    }
