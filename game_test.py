import pytest

from game import Game
from square_board import SquareBoard


def test_create():
    g = Game()
    assert g != None
    assert g.round_type != None
    assert g.match != None
    assert g.board != None
    assert g.board.is_full() == False


def test_has_winner_or_tie():
    game = Game()
    win_x = SquareBoard.fromList(
        [
            [
                "x",
                "o",
                None,
                None,
            ],
            [
                "o",
                "x",
                None,
                None,
            ],
            [
                "x",
                "o",
                "x",
                "o",
            ],
            [
                "x",
                "o",
                None,
                None,
            ],
        ]
    )

    win_o = SquareBoard.fromList(
        [
            [
                "x",
                "o",
                "x",
                "o",
            ],
            [
                "x",
                "x",
                "o",
                None,
            ],
            [
                "o",
                "o",
                None,
                None,
            ],
            [
                "o",
                "x",
                None,
                None,
            ],
        ]
    )

    tie = SquareBoard.fromList(
        [
            [
                "o",
                "x",
                "x",
                "o",
            ],
            [
                "x",
                "o",
                "o",
                "x",
            ],
            [
                "o",
                "x",
                "x",
                "o",
            ],
            [
                "x",
                "o",
                "o",
                "x",
            ],
        ]
    )

    unfinished = SquareBoard.fromList(
        [
            [
                "o",
                "x",
                "x",
                "o",
            ],
            [
                None,
                None,
                None,
                None,
            ],
            [
                None,
                None,
                None,
                None,
            ],
            [
                None,
                None,
                None,
                None,
            ],
        ]
    )

    game.board = win_x
    assert game.has_winner_or_tie() == True

    game.board = win_o
    assert game.has_winner_or_tie() == True

    game.board = tie
    assert game.has_winner_or_tie() == True

    game.board = unfinished
    assert game.has_winner_or_tie() == False
