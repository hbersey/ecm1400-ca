from monitoring_.panels._panel import DashboardPanel

class HomePanel(DashboardPanel):
    __LINES = """Welcome to the Air Quality Monitoring System.
Navigate around using the w, a, s and d keys.
Use the tab key to change column when entering dates.
To select an option, press enter.
To go back, press the escape key.""".splitlines()

    def _print(self, cols, lines, rh_size, rh_offset):
        n_cursor_up = (lines - 1 + len(self.__LINES)) // 2
        print(f"\033[{n_cursor_up}A")

        for line in self.__LINES:
            n_cursor_right = rh_offset + (rh_size - len(line)) // 2
            print(f"\033[{n_cursor_right}C{line}")
