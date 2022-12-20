import os


def clear_term() -> None:
    """Clears the terminal screen."""
    cmd = "cls" if os.name == "nt" else "clear"
    os.system(cmd)


def horizontal_rule(cols, char='-') -> None:
    """
    Prints a horizontal rule of the given length.

    Parameters
    ----------
    cols : int
        The length of the horizontal rule.
    char : str, optional
        The character to use for the horizontal rule, by default '-'
    """
    print(char * cols)


def layout(lh, selected, is_rh):
    """
    Prints the layout of the monitoring_.

    Parameters
    ----------
    lh : list
        The list of tuples containing the left-hand menu options.
    selected : int
        The index of the selected left-hand menu option.
    is_rh : bool
        Whether the right-hand menu is currently being interacted with.

    See Also
    --------
    clear_term : Clears the terminal screen.
    horizontal_rule : Prints a horizontal rule of the given length.
    """
    lh_names = [o[0] for o in lh]

    (cols, lines) = os.get_terminal_size()
    clear_term()

    horizontal_rule(cols)
    lines -= 1

    lh_max_size = len(sorted(lh_names, key=len, reverse=True)[
                      0]) + len(": NOT SELECTED")

    for i, lh_name in enumerate(lh_names):
        lh_selected_text = "SELECTED" if i == selected else "NOT SELECTED"
        lh = f"{lh_name}: {lh_selected_text}"

        lh_space_n = lh_max_size - len(lh) + 1
        lh_space = " " * lh_space_n
        rh_space = " " * (cols - lh_max_size - 5)

        style = "\033[1;30;47m" if (i == selected and is_rh == False) else ""

        print(f"| {style}{lh}\033[0m{lh_space}|{rh_space}|")

        lines -= 1

    lh_space = " " * (lh_max_size + 2)
    rh_space = " " * (cols - lh_max_size - 5)

    for _ in range(lines - 2):
        print(f"|{lh_space}|{rh_space}|")
    print(f"|{lh_space}|{rh_space}|", end="\r")

    horizontal_rule(cols)

    return lh_max_size
