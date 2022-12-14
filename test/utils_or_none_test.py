from utils import or_none


def test_sparse_or_none():
    assert or_none("Hello, World!") == "Hello, World!"
    assert or_none(None) == None
    assert or_none("") == None
