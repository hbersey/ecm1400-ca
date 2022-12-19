import dashboard.keys as keys

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