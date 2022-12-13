import dashboard.interface as if_
from utils import getch
import sys
from dashboard.panels import HomePanel


class Dashboard:
    __lh_state: int
    __rh_state: any
    __is_rh: bool

    def __init__(self):
        self.__lh_state = 0
        self.__rh_state = None
        self.__is_rh = False

    @property
    def __max_rh_state(self):
        return len(if_.OPTIONS) - 1

    def __lh_input(self):
        c = getch()
        if c == "w":
            self.__lh_state = max(0, self.__lh_state - 1)
        elif c == "s":
            self.__lh_state = min(self.__max_rh_state, self.__lh_state + 1)
        elif c == "d":
            pass
        elif c == "x":
            sys.exit(0)

    def __run(self):
        while True:
            lh_max_size = if_.layout(selected=self.__lh_state)
            HomePanel().print(lh_max_size)
            if not self.__is_rh:
                self.__lh_input()

    @staticmethod
    def run():
        dashboard = Dashboard()
        dashboard.__run()


if __name__ == "__main__":
    Dashboard.run()
