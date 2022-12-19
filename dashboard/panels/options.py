from dashboard.panels._panel import DashboardPanel
from dashboard.panels._components import LRSelect
import dashboard.keys as keys
from dashboard.species import Species
from dashboard.monitoring_data import MonitoringData


class OptionsPanel(DashboardPanel):

    __GROUP_SECTION = 0
    __SITE_SECTION = 1
    __SPECIES_SECTION = 2
    __N_SECTIONS = 3

    def __update_group_select(self):
        data = MonitoringData.instance()
        items = [k for k in data.groups]

        if self.group_select is None:
            self.group_select = LRSelect(items)
            return

        self.group_select.selected = min(
            self.group_select.selected, len(items) - 1)
        self.group_select.items = items

    def __update_site_select(self):
        data = MonitoringData.instance()
        items = [s.name for s in data.sites(
            data.group_name(self.group_select.selected))]

        if self.site_select is None:
            self.site_select = LRSelect(items)
            return

        self.site_select.selected = min(
            self.site_select.selected, len(items) - 1)
        self.site_select.items = items

    def __update_species_select(self):
        data = MonitoringData.instance()

        group_name = data.group_name(self.group_select.selected)
        sites = data.sites(group_name)
        if len(sites) == 0:
            self.__update_group_select()
            return
        species = data.species(sites[self.site_select.selected])
        items = [s.name for s in species]

        if self.species_select is None:
            self.species_select = LRSelect(items)
            return

        self.species_select.selected = min(
            self.species_select.selected, len(items) - 1)
        self.species_select.items = items

    def __init__(self) -> None:
        self.current_section = 0

        self.group_select = None
        self.__update_group_select()

        self.site_select = None
        self.__update_site_select()

        self.species_select = None
        self.__update_species_select()

    def _print(self, cols, lines, rh_size, rh_offset):

        n_cursor_up = lines - 1
        print(f"\033[{n_cursor_up}A")

        group_title_style = "\033[1;4m" if self.current_section == self.__GROUP_SECTION else ""
        print(f"\033[{rh_offset}C{group_title_style}Select Site Group:\033[0m")
        self.group_select.print(rh_offset, rh_size)

        site_title_style = "\033[1;4m" if self.current_section == self.__SITE_SECTION else ""
        print(f"\n\033[{rh_offset}C{site_title_style}Select Site:\033[0m")
        try:
            self.site_select.print(rh_offset, rh_size)
        except IndexError:
            self.__update_group_select()
            self.__update_site_select()
            self.site_select.print(rh_offset, rh_size)

        # Select Species
        species_title_style = "\033[1;4m" if self.current_section == self.__SPECIES_SECTION else ""
        print(
            f"\n\033[{rh_offset}C{species_title_style}Select Species:\033[0m")
        self.species_select.print(rh_offset, rh_size)

        print(f"\n\033[{rh_offset}CSelect Start Date:")

        print(f"\n\033[{rh_offset}CSelect End Date:")

    def handle_input(self, c):
        if c == keys.W and self.current_section > 0:
            self.current_section -= 1
            return
        elif c == keys.S and self.current_section < (self.__N_SECTIONS - 1):
            self.current_section += 1
            return

        if self.current_section == self.__GROUP_SECTION:
            self.group_select.handle_input(c)
            self.__update_site_select()
            self.__update_species_select()
        elif self.current_section == self.__SITE_SECTION:
            self.site_select.handle_input(c)
            self.__update_species_select()
        elif self.current_section == self.__SPECIES_SECTION:
            self.species_select.handle_input(c)
