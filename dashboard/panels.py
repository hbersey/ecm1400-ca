from abc import ABC, abstractmethod
import os


class DashboardPanel(ABC):
    @abstractmethod
    def get_initial_state(self):
        pass

    def print(self, lh_max_size):
        (cols, lines) = os.get_terminal_size()
        rh_offset = lh_max_size + 5
        rh_size = cols - rh_offset - 1
        self._print(cols, lines, rh_size, rh_offset)

    @abstractmethod
    def _print(self, cols, lines, rh_size, rh_offset):
        pass


class HomePanel(DashboardPanel):
    __LINES = """Welcome to the Air Quality Monitoring System.
Navigate the left hand menu using the w and s keys.
Then, press d to select the highlighted option, and enter the different pages.""".splitlines()

    def get_initial_state(self):
        return None

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1 + len(self.__LINES)) // 2
        print(f"\033[{n_cursor_up}A")

        for line in self.__LINES:
            n_cursor_right = rh_offset + (rh_size - len(line)) // 2
            print(f"\033[{n_cursor_right}C{line}")


class ExitPanel(DashboardPanel):
    __N_LINES = 3
    __S = "Are you sure you want to exit?"

    def get_initial_state(self):
        return False

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1 + self.__N_LINES) // 2
        print(f"\033[{n_cursor_up}A")

        n_cursor_right = rh_offset + (rh_size - len(self.__S)) // 2
        print(f"\033[{n_cursor_right}C{self.__S}")