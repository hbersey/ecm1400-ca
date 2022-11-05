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


def countvalue(values, xw):
    """Your documentation goes here"""
    # Your code goes here
