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

    def is_full ( self ):
        if len(self._line) == BOARD_LENGTH:
            print (len(self._line))
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

    def add ( self, x ):
        if len(self._line) < BOARD_LENGTH:
            self._line.append ( x )

    def is_tie ( self, x, o):
        tie = False
        if not find_streak (self._line, x) and not find_streak (self._line, o):
            tie = True
        return tie


