from datetime import datetime
import csv
import numpy as np


class MonitoringSite:
    def __init__(self, filename: str, type: str, coordinates_lat, coordinates_long, site_code: str):
        self.filename = filename
        self.type = type
        self.coordinates = (coordinates_lat, coordinates_long)
        self.site_code = site_code

    @property
    def path(self):
        return f"data/{self.filename}"

    @staticmethod
    def __parse_row(row):
        if row[1] == "24:00:00":
            # TODO: Am not sure this is what I should be doing.
            row[1] = "00:00:00"
        dt = datetime.fromisoformat(f"{row[0]}T{row[1]}")

        no = -1 if row[2] == "No data" else float(row[2])
        pm10 = -1 if row[3] == "No data" else float(row[3])
        pm25 = -1 if row[4] == "No data" else float(row[4])

        return dt, no, pm10, pm25

    def load(self):
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            data = np.array([MonitoringSite.__parse_row(row)
                            for row in reader])
            return data

    @staticmethod
    def with_sitecode(site_code: str):
        filtered = list(
            filter(lambda site: site.site_code == site_code, SITES))
        if len(filtered) == 0:
            raise ValueError(f"Site with site code {site_code} not found")
        return filtered[0]


MARYBONE_ROAD = MonitoringSite(
    "Pollution-London Marylebone Road.csv",
    "Urban Traffic",
    -0.154611, 51.52253,
    "MY1"
)

N_KENSINGTON = MonitoringSite(
    "Pollution-London N Kensington.csv",
    "Urban Background",
    -0.213492, 51.52105,
    "KC1"
)

HARLINGTON = MonitoringSite(
    "Pollution-London Harlington.csv",
    "Urban Industrial",
    -0.441614, 51.48879,
    "HRL"
)

SITES = [MARYBONE_ROAD, N_KENSINGTON, HARLINGTON]