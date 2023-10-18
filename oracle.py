from square_board import *
from settings import ColumnClassification

class ColumnRecommendation ():
    def __init__ (self, index, classification):
        self.index = index
        self.classification = classification

    def __repr__(self) -> str:
        return f'{self.__class__} index({self.index}), {self.classification}'
    
    def __eq__ (self, other):
        if not isinstance (other, self.__class__):
            return False
        return (self.index, self.classification) == (other.index, other.classification)
    
    def __hash__(self) -> int:
        return hash ((self.index, self.classification))
    
    def _set_classification(self, classification):
        self.classification = classification

class BaseOracle ():
    
    def get_recommendation (self, board, player):
        recommendation = []
        for i in range(len(board)):
            recommendation.append(self._get_column_recommendation(board, i, player))
        return recommendation

    def _get_column_recommendation (self, board, i, player):
        classification = ColumnRecommendation (i, ColumnClassification.MAYBE)
        if board._columns[i].is_full():
            classification._set_classification(ColumnClassification.FULL)
        return classification
