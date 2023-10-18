from oracle import BaseOracle, ColumnRecommendation
from settings import ColumnClassification

class Player ():

    def __init__(self, name, char, oracle = BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play (self, board):
        recommendation = self._oracle.get_recommendation (board, self)
        best = self._choose(recommendation)
        board.add (self.char, best.index)

    def _choose (self, recommendations):
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
        return valid[0]

        