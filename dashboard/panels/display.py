from dashboard.panels._panel import DashboardPanel
from dashboard.monitoring_data import MonitoringData
import requests
from dataclasses import dataclass
import pandas as pd
from dashboard.panels._components import HScroll
import numpy as np


@dataclass
class DPDataItem:
    ft: pd.Timestamp
    value: str


class DisplayPanel(DashboardPanel):
    def __init__(self) -> None:

        md = MonitoringData.instance()

        # site_code = md.site.code
        # species_code = md.species.code
        # start_date = md.start_date.strftime("%Y-%m-%d")
        # end_date = md.end_date.strftime("%Y-%m-%d")

        # res = requests.get(
        #     f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json")

        res = requests.get(
            "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode=BX2/SpeciesCode=NO2/StartDate=2022-10-20/EndDate=2022-12-20/Json")

        self.data = []
        self.no_values = True

        self.max_v = 0

        for item in res.json()["RawAQData"]["Data"]:
            v = item["@Value"]
            if len(v) > 0:
                self.no_values = False
                v = float(v)
                self.max_v = max(self.max_v, v)
            else:
                v = 0.0

            self.data.append(DPDataItem(
                pd.Timestamp(item["@MeasurementDateGMT"]),
                v
            ))

        # self.scroll = HScroll("")

    def _print(self, cols, lines, rh_size, rh_offset):
        if self.no_values:
            print("No values")
            return

        scale = self.max_v / (lines - 1)
        max_unit = int(self.max_v / scale)
        
        print(f"\033[{(lines - 1)}A")
        s = [f"\033[{rh_offset}C" for _ in range(max_unit)]

        for i, item in enumerate(self.data):
            if i > (rh_size):
                break

            u = int(item.value / scale)
            for y in range(max_unit):
                if y < u:
                    s[y] = f"{s[y]}█"
                else:
                    s[y] = f"{s[y]} "

        for l in reversed(s):
            print(l)
