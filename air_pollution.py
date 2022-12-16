import pandas as pd
import typing as t


NO_DATA_TEXT = "No data"  # Avoids magic string issues

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
    if s == NO_DATA_TEXT:
        return s
    return float(s)

# Not as efficient as it could be, but it's pandas didn't like my pervious solution:
# https://github.com/hbersey/ecm1400-ca/commit/272604370eca72bbc978b7590b8d0d8dda04d89c


def __read_csv(filename):
    data_df = pd.read_csv(
        f"data/{filename}", converters={3: __ap_float, 4: __ap_float, 5: __ap_float})
    dt_df = data_df.apply(lambda row: __ap_dt(
        row["date"], row["time"]), axis=1)
    return pd.concat([dt_df.rename("dt"), data_df.drop(["date", "time"], axis=1)], axis=1)


def load_data():
    hrl = __read_csv("Pollution-London Harlington.csv")
    my1 = __read_csv("Pollution-London Marylebone Road.csv")
    nk1 = __read_csv("Pollution-London N Kensington.csv")

    return {
        "HRL": hrl,
        "MY1": my1,
        "NK1": nk1
    }
