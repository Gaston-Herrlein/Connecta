from settings import *
from list_utils import *

class  LinearBoard():

    def __init__ ( self ):
        self._line = []

    def is_full ( self ):
        if self._line.__len__ () == BOARD_LENGTH:
            print (self._line.__len__)
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
        if self._line.__len__ () < BOARD_LENGTH:
            self._line.append ( x )

    def is_tie ( self, x, o):
        tie = False
        if not find_streak (self._line, x) and not find_streak (self._line, o):
            tie = True
        return tie


