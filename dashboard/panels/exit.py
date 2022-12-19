from dashboard.panels._panel import DashboardPanel
from dashboard.interface import clear_term
import dashboard.keys as keys

import sys

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