import typing as t

Numeric = t.Union[int, float]


def all_numerical_or_raise(values: t.List[t.Any]) -> None:
    """
    Checks if all values in an array are integers or floats.

    Parameters
    ----------
    values: list of any
        Values to be checked
    """
    if not all(map(lambda el: isinstance(el, (int, float)), values)):
        raise TypeError


def sumvalues(values: t.List[Numeric]) -> Numeric:
    """
    Returns the sum of all values in an array.

    Parameters
    ---------
    values: list of int or float
        Values to be summed

    Returns
    -------
    int or float
        The sum of ``values``. 
        Will return int if all ``values`` are int, otherwise float.
    """

    all_numerical_or_raise(values)

    total = 0
    for el in values:
        total += el
    return total


def maxvalue(values: t.List[Numeric]) -> Numeric:
    """
    Returns the maximum value from an array.

    Parameters
    ---------
    values: list of int or float
        Values to be checked for maximum

    Returns
    -------
    int or float
        The maximum value from ``values``. 
        Will return int if all values are int, otherwise float.
    """

    all_numerical_or_raise(values)

    val = values[0]
    for el in values:
        if el > val:
            val = el
    return val


def minvalue(values):
    """
    Returns the minimum value from an array.

    Parameters
    ---------
    values: list of int or float
        Values to be checked for minimum

    Returns
    -------
    int or float
        The minimum value from ``values``. 
        Will return int if all values are int, otherwise float.
    """

    all_numerical_or_raise(values)

    val = values[0]
    for el in values:
        if el < val:
            val = el
    return val


def meannvalue(values: t.List[Numeric]) -> float:
    """ 
    Returns the mean of ``values``.

    Parameters
    ---------
    values: list of int or float
        Values to be averaged

    Returns
    -------
    float
        The mean of ``values``. 

    """

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


def getch() -> int:
    """
    Takes a single character input, whithout having to wait for enter.

    Returns
    ------
    int
        Unicode value of the character; result of ord function.

    Credit
    ------
    Heavily based of Joe Esposito's code: 
    https://github.com/joeyespo/py-getch/blob/master/getch/getch.py
    """
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


T = t.TypeVar("T")


def parse_or_none(fn: t.Callable, s: t.Optional[str]) -> T:
    """
    Parses ``s`` using ``fn`` if  ``s`` is not None and is > 0

    Parmeters
    --------
    fn: function
        Function used for passing ``s``
    s: str
        Raw data to be passed

    Returns
    ------
    T or None
    """
    if s == None or len(s) == 0:
        return None

    try:
        return fn(s)
    except ValueError:
        return None


def or_none(s: t.Optional[str]) -> t.Optional[str]:
    """
    Returns ``s`` if not None and is > 0

    Parmeters
    --------
    s: str
        Raw data to be checked

    Returns
    ------
    T or None
    """
    if s == None or len(s) == 0:
        return None
    return s
