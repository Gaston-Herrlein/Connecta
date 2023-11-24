import pytest
from string_utils import *


def test_explode_string():
    assert explode_string("Han") == ["H", "a", "n"]
    assert explode_string("") == []


def test_explode_list_of_strings():
    assert explode_list_of_strings(["Han", "Solo"]) == [
        ["H", "a", "n"],
        ["S", "o", "l", "o"],
    ]
    assert explode_list_of_strings(["", "", ""]) == [[], [], []]
    assert explode_list_of_strings([]) == []


def test_explode_string_to_matrix():
    assert explode_string_to_matrix("Han|Solo") == [
        ["H", "a", "n"],
        ["S", "o", "l", "o"],
    ]
    assert explode_string_to_matrix("xox.|x...|oox.|....") == [
        ["x", "o", "x", None],
        ["x", None, None, None],
        ["o", "o", "x", None],
        [None, None, None, None],
    ]
    assert explode_string_to_matrix(["", "", ""]) == [[], [], []]
    assert explode_string_to_matrix([]) == []
