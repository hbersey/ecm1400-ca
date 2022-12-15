from abc import ABC, abstractmethod
import sys
import os
import dashboard.keys as keys
from dashboard.interface import clear_term
from dashboard.species import Species
from dashboard.sites import Site, SiteGroup


class DashboardPanel(ABC):
    def print(self, lh_max_size):
        (cols, lines) = os.get_terminal_size()
        rh_offset = lh_max_size + 5
        rh_size = cols - rh_offset - 1
        self._print(cols, lines, rh_size, rh_offset)

    @abstractmethod
    def _print(self, cols, lines, rh_size, rh_offset):
        pass

    def handle_input(self, c):
        pass


class HomePanel(DashboardPanel):
    __LINES = """Welcome to the Air Quality Monitoring System.
Navigate around using the w, a, s and d keys.
To select an option, press enter.
To go back, press the escape key.""".splitlines()

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1 + len(self.__LINES)) // 2
        print(f"\033[{n_cursor_up}A")

        for line in self.__LINES:
            n_cursor_right = rh_offset + (rh_size - len(line)) // 2
            print(f"\033[{n_cursor_right}C{line}")


class ExitPanel(DashboardPanel):
    __N_LINES = 3
    __S = "Are you sure you want to exit?"
    __BTN_GAP = 16

    def __init__(self) -> None:
        super().__init__()
        self.yes_selected = False

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1 + self.__N_LINES) // 2
        print(f"\033[{n_cursor_up}A")

        n_cursor_right = rh_offset + (rh_size - len(self.__S)) // 2
        print(f"\033[{n_cursor_right}C{self.__S}")

        n_cursor_right = rh_offset + (rh_size - self.__BTN_GAP - 13) // 2

        no_btn = "\033[30;47m  No  \033[0m" if not self.yes_selected else "  No  "
        yes_btn = "\033[30;47m  YES  \033[0m" if self.yes_selected else "  Yes  "

        s = no_btn + " " * self.__BTN_GAP + yes_btn

        print(f"\033[B\033[{n_cursor_right}C{s}")

    def handle_input(self, c):
        if self.yes_selected:
            if c == keys.ENTER:
                clear_term()
                sys.exit(0)
            elif c == keys.A:
                self.yes_selected = False
        elif c == keys.D and not self.yes_selected:
            self.yes_selected = True


class LRSelect:
    def __init__(self, items) -> None:
        self.items = items
        self.selected = 0

    def print(self, rh_offset, rh_size):
        larrow = "\033[6m<<\033[0m" \
            if self.selected > 0 \
            else "  "

        rarrow = "\033[6m>>\033[0m"  \
            if self.selected < len(self.items) - 1\
            else "  "

        item = self.items[self.selected]
        item_style = "\033[30;47m"

        print(
            f"\n\033[{rh_offset}C{larrow} {item_style} {item} \033[0m {rarrow}"),

    def handle_input(self, c):
        if c == keys.D and self.selected < (len(self.items) - 1):
            self.selected += 1
        elif c == keys.A and self.selected > 0:
            self.selected -= 1


class OptionsPanel(DashboardPanel):

    __GROUP_SECTION = 0
    __SITE_SECTION = 1
    __N_GROUPS = 2

    def __init__(self) -> None:
        self.current_section = 0

        self.groups = SiteGroup.get_all()
        self.group_select = LRSelect([group.name if len(
            group.description) > 16 else group.description for group in self.groups])
        self.selected_group = 0

        # self.sites = Site.get_site("All")
        self.sites = [Site(None, None, None, "Hello, World!", None,
                           None, None, None, None, None, None, None, None, None, None)]
        self.site_select = LRSelect([site.name for site in self.sites])

        self.species = Species.get_species()
        self.selected_specie = 0

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = lines - 1
        print(f"\033[{n_cursor_up}A")

        print(f"\033[{rh_offset}CSelect Site Group:")
        self.group_select.print(rh_offset, rh_size)

        print(f"\n\033[{rh_offset}CSelect Site:")

        # Select Species
        print(f"\n\033[{rh_offset}CSelect Species:")
        # for i, species in enumerate(self.species):
        #     print(f"\033[{rh_offset}C  {i + 1}. ", end="")
        #     if i == self.selected_specie:
        #         print("\033[1;4m", end="")
        #     print(f"{species.name}\033[0m")

        print(f"\n\033[{rh_offset}CSelect Start Date:")

        print(f"\n\033[{rh_offset}CSelect End Date:")

    def handle_input(self, c):
        if c == keys.W and self.current_section > 0:
            self.current_section -= 1
            return
        elif c == keys.D and self.current_section < (self.__N_GROUPS - 1):
            self.current_section += 1
            return

        if self.current_section == self.__GROUP_SECTION:
            self.group_select.handle_input(c)
        elif self.current_section == self.__SITE_SECTION:
            self.site_select.handle_input(c)
