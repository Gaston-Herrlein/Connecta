import pytest
from list_utils import *

def test_find_streak ():
    needle = 1
    none = [1, 0, 1, 1]
    none_beginning = [1, 'a', 1, 1, None] 
    beginning = [1, 1, 1, None]
    none_end = ['x', '0', 1, 1]
    end = ['0', 1, 1, 1]
    none_several = [0, 0, 3, 4, 1, 3, 2, 1, 3, 4]
    several = [0, 0, 3, 1, 1, 1, 1, 2, None, 3, 4]

    assert find_streak(none, needle) == False
    assert find_streak(none_beginning, needle) == False
    assert find_streak(none_end, needle) == False
    assert find_streak(none_several, needle) == False
    assert find_streak(beginning, needle)
    assert find_streak(end, needle)
    assert find_streak(several, needle)
    #Test para el caso en que se pida un numero de ocurrencias distinta a "VICTORY_STRICK"
    assert find_streak([0, 'a', None, 1, 1, 1, 1, 1], needle, 5)