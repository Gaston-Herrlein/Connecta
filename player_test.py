import pytest

from square_board import SquareBoard
from oracle import BaseOracle
from player import Player, _is_non_full_column, _is_int, _is_within_column_range


def test_play ():
    before = SquareBoard.fromList([[None, None, None, None],
                                   ['x', 'o', 'x', 'o'],
                                   ['o', 'o', None, None],
                                   ['x', 'x', None, None]])
    
    after = SquareBoard.fromList([['x', None, None, None],
                                   ['x', 'o', 'x', 'o'],
                                   ['o', 'o', None, None],
                                   ['x', 'x', None, None]])
    
    player = Player ('CR7', 'x', oracle = BaseOracle())
    player.play(before)

    assert before == after

def test_valid_column():
    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])

    assert _is_within_column_range(0)
    assert _is_within_column_range(1)
    assert _is_within_column_range(2)
    assert _is_within_column_range(3)
    assert _is_within_column_range(5) == False
    assert _is_within_column_range(-10) == False
    assert _is_within_column_range(10) == False

def test_is_non_full_column():
    board = SquareBoard.fromList([['x', None, None, None, ],
                                  ['x', 'o', 'x', 'o', ],
                                  ['o', 'o', 'x', 'x', ],
                                  ['o', None, None, None, ]])
                                
    assert _is_non_full_column(board, 0)
    assert _is_non_full_column(board, 1) == False
    assert _is_non_full_column(board, 2) == False
    assert _is_non_full_column(board, 3) 

def test_is_int():
    assert _is_int('42')
    assert _is_int('0')
    assert _is_int('-32')
    assert _is_int('  32   ')
    assert _is_int('hola') == False
    assert _is_int('') == False
    assert _is_int('3.14') == False