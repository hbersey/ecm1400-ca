import dashboard.keys as keys
import pandas as pd


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


class DateInput:
    def __init__(self, date=pd.Timestamp.now()) -> None:
        self.date = date
        self.current_day = self.date.day
        self.current_month = self.date.month
        self.current_year = self.date.year
        self.current_section = 0

    def print(self, rh_offset):
        day_style = "\033[30;47m" if self.current_section == 0 else ""
        month_style = "\033[30;47m" if self.current_section == 1 else ""
        year_style = "\033[30;47m" if self.current_section == 2 else ""

        print(f"\n\033[{rh_offset}C{day_style} {self.current_day} \033[0m / {month_style} {self.current_month} \033[0m / {year_style} {self.current_year} \033[0m")

    def handle_input(self, c):
        if c == keys.TAB:
            self.current_section = (self.current_section + 1) % 3
        elif (c == keys.A or c == keys.D):
            delta = 1 if c == keys.D else -1
            if self.current_section == 0:
                ts = pd.Timestamp(self.current_year,
                                  self.current_month, self.current_day)
                new_day = self.current_day + delta
                if new_day < 1:
                    if self.current_month == 1:
                        self.current_year -= 1
                        self.current_month = 12
                    else:
                        self.current_month -= 1
                    self.current_day = pd.Timestamp(
                        self.current_year, self.current_month, 1).days_in_month
                elif new_day > ts.days_in_month:
                    if self.current_month == 12:
                        self.current_year += 1
                        self.current_month = 0
                    self.current_month += 1
                    self.current_day = 1
                else:
                    self.current_day = new_day

            elif self.current_section == 1:
                new_month = self.current_month + delta
                if new_month < 1:
                    new_month = 12
                    self.current_year -= 1
                elif new_month > 12:
                    new_month = 1
                    self.current_year += 1
                self.current_month = new_month

            elif self.current_section == 2:
                self.current_year = max(
                    1, min(9999, self.current_year + delta))
