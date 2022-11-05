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


def minvalue(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)


def meannvalue(values):
    """Your documentation goes here"""

    all_numerical_or_raise(values)


def countvalue(values, xw):
    """Your documentation goes here"""
    # Your code goes here
