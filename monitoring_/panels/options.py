from monitoring_.panels._panel import DashboardPanel
from monitoring_.panels._components import *
import monitoring_.keys as keys
from monitoring_.species import Species
from monitoring_.monitoring_data import MonitoringData


class OptionsPanel(DashboardPanel):

    __GROUP_SECTION = 0
    __SITE_SECTION = 1
    __SPECIES_SECTION = 2
    __START_DATE_SECTION = 3
    __END_DATE_SECTION = 4
    __N_SECTIONS = 5

    def __update_group_select(self):
        data = MonitoringData.instance()
        items = [k for k in data.groups]

        if self.group_select is None:
            def get_selected():
                return data.selected_group

            def set_selected(val):
                data.selected_group = val

            self.group_select = LRSelect(items, get_selected, set_selected)
            return

        data.selected_group = min(data.selected_group, len(items) - 1)
        self.group_select.items = items

    def __update_site_select(self):
        data = MonitoringData.instance()
        items = [s.name for s in data.sites(
            data.group_name(data.selected_group))]

        if self.site_select is None:
            def get_selected():
                return data.selected_site

            def set_selected(val):
                data.selected_site = val

            self.site_select = LRSelect(items, get_selected, set_selected)
            return

        data.selected_site = min(data.selected_site, len(items) - 1)
        self.site_select.items = items

    def __update_species_select(self):
        data = MonitoringData.instance()

        group_name = data.group_name(data.selected_group)
        sites = data.sites(group_name)
        if len(sites) == 0:
            self.__update_group_select()
            return
        species = data.get_species(sites[data.selected_site])
        items = [s.name for s in species]

        if self.species_select is None:
            def get_selected():
                return data.selected_species

            def set_selected(val):
                data.selected_species = val

            self.species_select = LRSelect(items, get_selected, set_selected)
            return

        data.selected_species = min(data.selected_species, len(items) - 1)
        self.species_select.items = items

    def __init__(self) -> None:
        self.current_section = 0

        self.group_select = None
        self.__update_group_select()

        self.site_select = None
        self.__update_site_select()

        self.species_select = None
        self.__update_species_select()

        def get_start_date():
            return MonitoringData.instance().start_date

        def set_start_date(val):
            MonitoringData.instance().start_date = val

        self.start_date = DateInput(get_start_date, set_start_date)

        def get_end_date():
            return MonitoringData.instance().end_date

        def set_end_date(val):
            MonitoringData.instance().end_date = val
            
        self.end_date = DateInput(get_end_date, set_end_date)

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

        start_date_style = "\033[1;4m" if self.current_section == self.__START_DATE_SECTION else ""
        print(
            f"\n\033[{rh_offset}C{start_date_style}Select Start Date:\033[0m")
        self.start_date.print(rh_offset)

        end_date_style = "\033[1;4m" if self.current_section == self.__END_DATE_SECTION else ""
        print(f"\n\033[{rh_offset}C{end_date_style}Select End Date:\033[0m")
        self.end_date.print(rh_offset)

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
        elif self.current_section == self.__START_DATE_SECTION:
            self.start_date.handle_input(c)
        elif self.current_section == self.__END_DATE_SECTION:
            self.end_date.handle_input(c)
