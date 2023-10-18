from oracle import *
from square_board import *
from settings import ColumnClassification


def test_base_oracle():
    board = SquareBoard.fromList([[None, None, None, None]])
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE)]

    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected

def test_equality ():
    cr = ColumnRecommendation(2, ColumnClassification.MAYBE)

    assert cr == cr  
    assert cr == ColumnRecommendation(2, ColumnClassification.MAYBE)  

    assert cr != ColumnRecommendation(2, ColumnClassification.FULL)
    assert cr != ColumnRecommendation(3, ColumnClassification.MAYBE)
    assert cr != ColumnRecommendation(3, ColumnClassification.FULL)
