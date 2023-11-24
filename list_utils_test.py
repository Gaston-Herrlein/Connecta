import pytest
from list_utils import *
from settings import ColumnClassification
from oracle import ColumnRecommendation


def test_find_streak():
    needle = 1
    none = [1, 0, 1, 1]
    none_beginning = [1, "a", 1, 1, None]
    beginning = [1, 1, 1, None]
    none_end = ["x", "0", 1, 1]
    end = ["0", 1, 1, 1]
    none_several = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]
    several = [0, 0, 3, 1, 1, 1, 1, 2, None, 3, 4]

    assert find_streak(none, needle) == False
    assert find_streak(none_beginning, needle) == False
    assert find_streak(none_end, needle) == False
    assert find_streak(none_several, needle) == False
    assert find_streak(beginning, needle)
    assert find_streak(end, needle)
    assert find_streak(several, needle)
    # Test para el caso en que se pida un numero de ocurrencias distinta a "VICTORY_STRICK"
    assert find_streak([0, "a", None, 1, 1, 1, 1, 1], needle, 5)


def test_nth_elements():
    original = [[1, 2, 3], [0, 0, 0], ["a", 8, 9]]

    assert nth_elements(original) == [1, 0, "a"]
    assert nth_elements(original, 1) == [2, 0, 8]
    assert nth_elements(original, 2) == [3, 0, 9]


def test_transpose():
    original = [[1, 2, 3], [4, 5, 6]]
    transposed = [[1, 4], [2, 5], [3, 6]]

    assert transpose(original) == transposed
    assert transpose(transpose(original)) == original


def test_one_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [["a", "b"], [1, None], [8, 9]]

    assert one_displace(l1) == [6, 1, 2, 3, 4, 5]
    assert one_displace(l2) == [[8, 9], ["a", "b"], [1, None]]


def test_displace():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [["a", "b"], [1, None], [8, 9]]

    assert displace([]) == []
    assert displace(l1, 1) == [None, 1, 2, 3, 4, 5]
    assert displace(l1, 2) == [None, None, 1, 2, 3, 4]
    assert displace(l2, 1) == [None]
    assert displace(l3) == [["a", "b"], [1, None], [8, 9]]
    assert displace(l3, 1) == [None, ["a", "b"], [1, None]]


def test_reverse_list():
    l1 = [1, 2, 3, 4, 5, 6]
    l2 = [1]
    l3 = [["a", "b"], [1, None], [8, 9]]

    assert reverse_list(l1) == [6, 5, 4, 3, 2, 1]
    assert reverse_list(l2) == [1]
    assert reverse_list(l3) == [[8, 9], [1, None], ["a", "b"]]


def test_reverse_matrix():
    l1 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    l2 = [["a", "b"], [1, None], [8, 9]]

    assert reverse_matrix(l1) == [
        [3, 2, 1, 0],
        [7, 6, 5, 4],
        [11, 10, 9, 8],
        [15, 14, 13, 12],
    ]
    assert reverse_matrix(l2) == [["b", "a"], [None, 1], [9, 8]]


def test_all_same():
    l1 = [0, 1, 32, 3, 4]
    l2 = [["a", "b"], [1, None], [8, 9]]
    l3 = [["a", "b"], ["a", "b"], ["a", "b"]]
    l4 = [
        ColumnRecommendation(1, ColumnClassification.MAYBE),
        ColumnRecommendation(2, ColumnClassification.MAYBE),
    ]
    l5 = [
        ColumnRecommendation(1, ColumnClassification.FULL),
        ColumnRecommendation(1, ColumnClassification.MAYBE),
    ]

    assert all_same(l1) == False
    assert all_same(l2) == False
    assert all_same(l3)
    assert all_same(l4)
    assert all_same(l5) == False


def test_collapse_list():
    assert collapse_list([]) == ""
    assert collapse_list(["o", "x", "x", "o"]) == "oxxo"
    assert collapse_list(["x", "x", None, None, None]) == "xx..."


def test_collapse_matrix():
    assert collapse_matrix([]) == ""
    assert (
        collapse_matrix([["x", "x", None], ["o", "x", "x"], ["o", None, None]])
        == "xx.|oxx|o.."
    )


def test_replace_all_in_list():
    assert replace_all_in_list([None, 3, "546", 33, None], None, "#") == [
        "#",
        3,
        "546",
        33,
        "#",
    ]
    assert replace_all_in_list([1, 2, 3, 4, 5], "e", 42) == [1, 2, 3, 4, 5]
    assert replace_all_in_list([], 34, 43) == []


def test_replace_all_in_matrix():
    assert replace_all_in_matrix(
        [[1, 2, 3, "n", "n", None], [4, 5, "n"]], "n", "#"
    ) == [[1, 2, 3, "#", "#", None], [4, 5, "#"]]

    assert replace_all_in_matrix([[None, None, 2, True], [4, 5, "#"]], "k", 42) == [
        [None, None, 2, True],
        [4, 5, "#"],
    ]

    assert replace_all_in_matrix([], None, 7) == []
    assert replace_all_in_matrix([[], []], None, 7) == [[], []]
