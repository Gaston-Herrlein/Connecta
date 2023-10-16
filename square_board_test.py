import pytest

from square_board import *

def test_empty_board ():
    board = SquareBoard ()

    assert board.is_full () == False
    assert board.is_victory ('x') == False
    assert board.is_victory ('o') == False


def test_as_matrix ():
    matrix = [['o', 'x', 'x', 'x', ],
                [None, None, None, None, ],
                [None, None, None, None, ],
                [None, None, None, None, ],
                [None, None, None, None, ]]

    board = SquareBoard.fromList(matrix)

    assert board.as_matrix() == matrix

def test_vertical_victory():
    vertical = SquareBoard.fromList([['o', 'x', 'x', 'x', ],
                                     [None, None, None, None, ],
                                     [None, None, None, None, ],
                                     [None, None, None, None, ]])
    assert vertical.is_victory('x')
    assert vertical.is_victory('o') == False


def test_horizontal_victory():
    horizontal_victory = SquareBoard.fromList([['x', None, None, None, ],
                                               ['x', None, None, None, ],
                                               ['x', 'o', None, None, ],
                                               ['x', 'o', None, None, ]])

    assert horizontal_victory.is_victory('x')
    assert horizontal_victory.is_victory('o') == False

def test_sinking_victory():
    sinking_victory = SquareBoard.fromList([['x', 'o', 'x', 'o', ],
                                            ['x', 'x', 'o', None, ],
                                            ['o', 'o', None, None, ],
                                            ['o', 'x', None, None, ]])
    assert sinking_victory.is_victory('x') == False
    assert sinking_victory.is_victory('o')

def test_rising_victory():
    rising_victory = SquareBoard.fromList([['x', 'o', None, None, ],
                                           ['o', 'x', None, None, ],
                                           ['x', 'o', 'x', 'o', ],
                                           ['x', 'o', None, 'x', ]])
    assert rising_victory.is_victory('x')
    assert rising_victory.is_victory('o') == False