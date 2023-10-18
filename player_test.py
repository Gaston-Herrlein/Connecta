import pytest

from square_board import SquareBoard
from oracle import BaseOracle
from player import Player


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
