import monitoring_.interface as if_
from utils import getch
import sys
import monitoring_.keys as keys

from monitoring_.panels._panel import DashboardPanel
from monitoring_.panels.home import HomePanel
from monitoring_.panels.options import OptionsPanel
from monitoring_.panels.about import AboutPanel
from monitoring_.panels.display import DisplayPanel
from monitoring_.panels.exit import ExitPanel

LH = [
    ["Home", HomePanel],
    ["Options", OptionsPanel],
    ["About", AboutPanel],
    ["Display", DisplayPanel],
    ["Exit", ExitPanel],
]


class Dashboard:
    __lh_state: int
    __rh: DashboardPanel
    __is_rh: bool

    def __init__(self):
        self.__lh_state = 0
        self.__rh = None
        self.__is_rh = False

    @property
    def __max_rh_state(self):
        return len(LH) - 1

    def __lh_input(self):
        c = getch()
        prev_lh_state = self.__lh_state

        if c == keys.W:
            self.__lh_state = max(0, self.__lh_state - 1)
        elif c == keys.S:
            self.__lh_state = min(self.__max_rh_state, self.__lh_state + 1)
        elif c == keys.D or c == keys.ENTER:
            self.__is_rh = True
        elif c == keys.X:
            sys.exit(0)

        if prev_lh_state != self.__lh_state:
            self.__rh = None

    def __rh_input(self):
        c = getch()

        if c == keys.ESC:
            self.__is_rh = False

        self.__rh.handle_input(c)

    def __run(self):
        while True:
            lh_max_size = if_.layout(LH, self.__lh_state, self.__is_rh)
            if self.__rh is None:
                self.__rh = LH[self.__lh_state][1]()
            self.__rh.print(lh_max_size)

            (self.__rh_input if self.__is_rh else self.__lh_input)()

    @staticmethod
    def run():
        dashboard = Dashboard()
        dashboard.__run()
