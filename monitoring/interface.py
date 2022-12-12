import os
import sys


def clear_term():
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)


def horizontal_rule(cols, char='-'):
    print(char * cols)


CLEAR_STYLE = "\033[0m"

CURSOR_UP = "\033[A"
CURSOR_RIGHT = "\033[C"

# LHAND = [
#     "Site: NOT SELECTED",
#     "Species: NOT SELECTED",
#     "Start Date: NOT SELECTED",
#     "End Data: NOT SELECTED"
# ]


def home_page():
    return [
        "Welcome to the Air Quality Monitoring System",
        "Navigate the left hand menu using the w and s keys.",
        "Then, press d to select the highlighted option, and enter the different pages.",
    ]


def exit_page():
    return [
        "Are you sure you want to exit?",
    ]


OPTIONS = [
    ["Home", home_page],
    ["Site", lambda: []],
    ["Species", lambda: []],
    ["Start", lambda: []],
    ["End", lambda: []],
    ["Exit", exit_page],
]
OPTION_NAMES = [o[0] for o in OPTIONS]

EXIT_INDEX = 5

# https://github.com/joeyespo/py-getch/blob/master/getch/getch.py


def getch():
    try:
        import msvcrt
        return msvcrt.getch()
    except ImportError:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def home(selected=0):
    (cols, lines) = os.get_terminal_size()
    clear_term()

    horizontal_rule(cols)
    lines -= 1

    lh_max_size = len(sorted(OPTION_NAMES, key=len, reverse=True)[
                      0]) + len(": NOT SELECTED")

    for i, lh_name in enumerate(OPTION_NAMES):
        lh_selected_text = "SELECTED" if i == selected else "NOT SELECTED"
        lh = f"{lh_name}: {lh_selected_text}"

        lh_space_n = lh_max_size - len(lh) + 1
        lh_space = " " * lh_space_n
        rh_space = " " * (cols - lh_max_size - 5)

        style = "\033[1;30;47m" if i == selected else ""

        print(f"| {style}{lh}{CLEAR_STYLE}{lh_space}|{rh_space}|")

        lines -= 1

    lh_space = " " * (lh_max_size + 2)
    rh_space = " " * (cols - lh_max_size - 5)

    for _ in range(lines - 2):
        print(f"|{lh_space}|{rh_space}|")
    print(f"|{lh_space}|{rh_space}|", end="\r")

    horizontal_rule(cols)

    rh_offset = lh_max_size + 5

    (cols, lines) = os.get_terminal_size()
    rh_lines = OPTIONS[selected][1]()

    n_cursor_up = (lines - 1 + len(rh_lines)) // 2
    print(CURSOR_UP * n_cursor_up, end="")

    for line in rh_lines:
        print(CURSOR_RIGHT * rh_offset, end="")
        print(line)

    sel = getch()
    if sel == "w":
        selected = max(0, selected - 1)
    elif sel == "s":
        selected = min(len(OPTIONS) - 1, selected + 1)
    elif sel == "d":
        pass
    elif sel == "x":
        clear_term()
        sys.exit(0)
        return

    clear_term()
    home(selected)


home()
clear_term()
