def sumvalues(values):
    """Your documentation goes here"""

    if not all(map(lambda el: isinstance(el, (int, float)), values)):
        raise TypeError

    total = 0
    for el in values:
        total += el
    return total


def maxvalue(values):
    """Your documentation goes here"""
    # Your code goes here


def minvalue(values):
    """Your documentation goes here"""
    # Your code goes here


def meannvalue(values):
    """Your documentation goes here"""
    # Your code goes here


def countvalue(values, xw):
    """Your documentation goes here"""
    # Your code goes here
