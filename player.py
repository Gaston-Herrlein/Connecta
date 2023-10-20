from oracle import BaseOracle, ColumnRecommendation
from square_board import SquareBoard

from settings import ColumnClassification, BOARD_LENGTH

def _is_within_column_range (col):
    return (col>=0 and col < BOARD_LENGTH) 
    
def _is_non_full_column (board, col):
    return not board._columns[col].is_full()

def _is_int (col):
    try:
        nume = int(col)
        return True
    except:
        return False 

class Player ():
    def __init__(self, name, char, oracle = BaseOracle()) -> None:
        self.name = name
        self.char = char
        self._oracle = oracle

    def play (self, board):
        (best, recommendation) = self._ask_oracle (board)
        self._play_on (board, best.index)
    
    def _play_on (self, board, index):
        board.add (self.char, index)

    def _ask_oracle (self, board):
        recommendation = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendation)
        return (best, recommendation)

    def _choose (self, recommendations):
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
        return valid[0]

class HumanPlayer (Player):
    def __init__ (self, name, char):
        super.__init__(name, char)
    
    def _ask_oracle (self, board):
        while True:
            raw = input ("Selecciona una columna: ")
            validation = _is_int(raw) and _is_within_column_range (int(raw)) and _is_non_full_column (int(raw))
            if validation:
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)
            