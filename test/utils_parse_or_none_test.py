from utils import parse_or_none


def test_sparse_or_none():
    assert parse_or_none(int, "12") == 12
    assert parse_or_none(int, None) == None
    assert parse_or_none(int, "") == None
