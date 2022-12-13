def all_numerical_or_raise(values):
    if not all(map(lambda el: isinstance(el, (int, float)), values)):
        raise TypeError


def sumvalues(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)

    total = 0
    for el in values:
        total += el
    return total


def maxvalue(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)

    val = values[0]
    for el in values:
        if el > val:
            val = el
    return val


def minvalue(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)

    val = values[0]
    for el in values:
        if el < val:
            val = el
    return val


def meannvalue(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)
    return sumvalues(values) / len(values)


def countvalue(values, x):
    """Your documentation goes here"""

    n = 0
    for el in values:
        # not sure if 3.0 shoud be counted as the same as 3. I am not counting it a the moment.
        # TODO: Follow up
        if type(el) == type(x) and el == x:
            n += 1
    return n


def getch():
    try:
        import msvcrt
        c = msvcrt.getch()
    except ImportError:
        import tty
        import termios
        import sys
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            c = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ord(c)