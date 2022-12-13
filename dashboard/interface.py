import os

def clear_term():
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)


def horizontal_rule(cols, char='-'):
    print(char * cols)

CURSOR_UP = "\033[A"
CURSOR_RIGHT = "\033[C"


def home_page(_):
    return [
        "Welcome to the Air Quality Monitoring System",
        "Navigate the left hand menu using the w and s keys.",
        "Then, press d to select the highlighted option, and enter the different pages.",
    ]


def exit_page(yn_selected):
    no_btn = "\033[30;47m  No  \033[0m" if yn_selected == 0 else "  No  "
    yes_btn = "\033[30;47m  YES  \033[0m" if yn_selected == 1 else "  Yes  "

    buttons = no_btn + " " * 8 + yes_btn

    return [
        "Are you sure you want to exit?",
        "",
        [buttons, 21]
    ]


OPTIONS = [
    ["Home", home_page],
    ["Site", lambda _: []],
    ["Species", lambda _: []],
    ["Start", lambda _: []],
    ["End", lambda _: []],
    ["Exit", exit_page],
]
OPTION_NAMES = [o[0] for o in OPTIONS]

EXIT_INDEX = 5

# https://github.com/joeyespo/py-getch/blob/master/getch/getch.py


def layout(selected=0):
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

        print(f"| {style}{lh}\033[0m{lh_space}|{rh_space}|")

        lines -= 1

    lh_space = " " * (lh_max_size + 2)
    rh_space = " " * (cols - lh_max_size - 5)

    for _ in range(lines - 2):
        print(f"|{lh_space}|{rh_space}|")
    print(f"|{lh_space}|{rh_space}|", end="\r")

    horizontal_rule(cols)

    return lh_max_size