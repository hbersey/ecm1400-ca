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
