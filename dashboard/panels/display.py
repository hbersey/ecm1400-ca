from dashboard.panels._panel import DashboardPanel
from dashboard.monitoring_data import MonitoringData
import requests
from dataclasses import dataclass
import pandas as pd
import dashboard.keys as keys


@dataclass
class DPDataItem:
    ft: pd.Timestamp
    value: str


class DisplayPanel(DashboardPanel):
    def __init__(self) -> None:

        self.x_pos = 0
        md = MonitoringData.instance()

        site_code = md.site.code
        species_code = md.species.code
        start_date = md.start_date.strftime("%Y-%m-%d")
        end_date = md.end_date.strftime("%Y-%m-%d")

        res = requests.get(
            f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json")

        # res = requests.get(
        #     "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode=BX2/SpeciesCode=NO2/StartDate=2022-10-20/EndDate=2022-12-20/Json")

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
            print(f"\033[{(lines - 2)}A")
            print(f"\033[{rh_offset}C No data available for current selection")
            print(f"\033[{rh_offset}C Try bexley > Bexley - Belvedere > NO2 for an example")

            return
        height = lines - 5
        width = rh_size - 2

        y_axis_width = 5
        x_axis_height = 3

        graph_width = width - y_axis_width
        graph_height = height - x_axis_height

        scale = self.max_v / graph_height

        print(f"\033[{(lines - 2)}A")
        s = [f"\033[{rh_offset}C" for _ in range(graph_height)]

        # Print y axis
        for i in range(graph_height):
            if i % 3 == 0:
                n = f"{(i * scale):.1f}".rjust(4)
                s[i] = f"{s[i]}{n} "
            else:
                space = " " * y_axis_width
                s[i] = f"{s[i]}{space}"

        # Plot Graph
        for i in range(len(self.data)):
            if i > (graph_width):
                break

            item = self.data[i + self.x_pos]

            u = int(item.value / scale)
            for y in range(graph_height):
                if y < u:
                    s[y] = f"{s[y]}█"
                else:
                    s[y] = f"{s[y]} "

        # Print Graph
        for l in reversed(s):
            print(l)

        # Print x axis
        x_axis_lines = ["" for _ in range(3)]

        for i in range(len(self.data)):
            if i % 10 == 0:
                x_axis_lines[0] = f"{x_axis_lines[0]}\\"

                d = self.data[i].ft

                l2 = d.strftime("%H:%M")
                l1 = d.strftime("%d-%m")

                x_axis_lines[1] = f"{x_axis_lines[1]}{l1}     "
                x_axis_lines[2] = f"{x_axis_lines[2]}{l2}     "
            else:
                x_axis_lines[0] = f"{x_axis_lines[0]} "

        for i in range(3):
            print(
                f"\033[{(rh_offset + y_axis_width)}C{x_axis_lines[i][self.x_pos : self.x_pos + graph_width]}")

    def handle_input(self, c):
        if c == keys.A and self.x_pos > 0:
            self.x_pos -= 1
        elif c == keys.D and self.x_pos < len(self.data):
            self.x_pos += 1
