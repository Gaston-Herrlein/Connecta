from settings import *
from list_utils import *

class  LinearBoard():

    @classmethod
    def fromList(cls, list):
        column = cls()
        if len(list) <= BOARD_LENGTH:    
            column._line = list
        return column

    def __init__ ( self ):
        self._line = []

    def __eq__ (self, other):
        if not isinstance (other, self.__class__):
            return False
        else:
            return self._line == other._line
        
    def __hash__(self) -> int:
        return hash (self._line)

    def __repr__(self) -> str:
        return f'{self._line}'    

    def is_full ( self ):
        line_aux = list(filter(lambda x: x != None, self._line))
        if len(line_aux) == BOARD_LENGTH:
            return True
        return False

    def is_victory ( self, x ):
        if self._line.count( x ) >= VICTORY_STRICK:
            count = 0
            for i in self._line:
                if i == x:
                    count += 1
            if count >= VICTORY_STRICK:
                return True
        return False

    def add ( self, char ):
        if not self.is_full():
            i = self._line.index(None)
            self._line[i] = char

    def is_tie ( self, x, o):
        tie = False
        if not find_streak (self._line, x) and not find_streak (self._line, o):
            tie = True
        return tie


