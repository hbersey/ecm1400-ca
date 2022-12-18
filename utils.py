import typing as t
import numpy as np

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


class NDQueue:
    def __init__(self, initial_size=16, growth_factor=1.5, dtype=None):
        self.__items = np.zeros(initial_size, dtype=dtype)
        self.__tail = 0
        self.__head = 0
        self.__growth_factor = growth_factor
        self.__dtype = dtype

    def enqueue(self, item):
        if self.__tail == len(self.__items):
            if self.__head > 0:
                self.__items[: self.__tail -
                             self.__head] = self.__items[self.__head: self.__tail]
                self.__tail -= self.__head
                self.__head = 0
            else:
                new_size = int(len(self.__items) * self.__growth_factor)
                new_items = np.zeros(new_size, dtype=self.__dtype)
                new_items[: len(self.__items)] = self.__items
                self.__items = new_items

        try:
            self.__items[self.__tail] = item
        except ValueError:
            raise ValueError(
                f"Item must be of type {self.dtype}, not {type(item)}")

        self.__tail += 1

    def dequeue(self):
        if self.__head == self.__tail:
            raise IndexError("Queue is empty")
        item = self.__items[self.__head]
        self.__head += 1
        return item

    def is_empty(self):
        return self.__head == self.__tail


def __quick_sort_partition(at, swap, low, high):
    i = low - 1
    pivot = at(high)

    for j in range(low, high):
        if at(j) <= pivot:
            i += 1
            swap(i, j)

    swap(i + 1, high)
    return i + 1


def quick_sort(at, swap, low, high):
    if low >= high:
        return

    pivot_index = __quick_sort_partition(at, swap, low, high)
    quick_sort(at, swap, low, pivot_index - 1)
    quick_sort(at, swap, pivot_index + 1, high)


def menu(title: str, items: t.List[t.Tuple[str, str, t.Optional[t.Callable]]]):
    fns = {}

    print(f"\n{title}")
    print("-" * len(title), end="\n\n")

    for (option, description, *fn) in items:
        print(f"{option}) {description}")
        fns[option] = fn[0] if len(fn) == 1 else lambda: None

    print()

    while True:
        sel = input("Your selection: ").strip()
        if sel in fns.keys():
            fns[sel]()
            break
        print("\nInvalid selection. Please try again.")

    return sel
