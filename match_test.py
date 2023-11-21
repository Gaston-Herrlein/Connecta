import pytest
from player import Player
from match import Match

jrr_10 = None
cr_7 = None


def setup():
    global jrr_10
    jrr_10 = Player("Riquelme")
    global cr_7
    cr_7 = Player("Ronaldo")


def teardown():
    global jrr_10
    jrr_10 = None
    global cr_7
    cr_7 = None


def test_different_player_have_different_char():
    m = Match(jrr_10, cr_7)
    assert jrr_10.char != cr_7.char


def test_no_player_with_none_char():
    m = Match(jrr_10, cr_7)

    assert jrr_10.char != None
    assert cr_7.char != None


def test_next_player_is_round_robbin():
    m = Match(jrr_10, cr_7)
    p1 = m.next_player
    p2 = m.next_player

    assert p1 != p2


def test_player_are_opponents():
    m = Match(jrr_10, cr_7)
    p1 = m.next_player
    p2 = m.next_player

    assert p1.opponent == p2
    assert p2.opponent == p1
