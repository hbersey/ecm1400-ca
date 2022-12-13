from abc import ABC, abstractmethod
import os


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
