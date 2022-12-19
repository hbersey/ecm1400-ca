from dashboard.panels._panel import DashboardPanel
import requests

class DisplayPanel(DashboardPanel):
    def __init__(self) -> None:
        res = requests.get(f"https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode=BX5/SpeciesCode=NO/StartDate=2021-09-20/EndDate=2021-09-30/Json")

    def _print(self, cols, lines, rh_size, rh_offset):
        pass
