from linear_board import *
from list_utils import *
from settings import *

class SquareBoard ():

    @classmethod
    def fromList(cls, list_of_lists):
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    def __init__ (self):
        self._columns = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def __repr__ (self):
        return f'{self.__class__}: {self._columns}'
    
    def __len__ (self):
        return len (self._columns)
    
    def __eq__ (self, other):
        if not isinstance (other, self.__class__):
            return False
        else:
            return self._columns == other._columns
        
    def __hash__(self) -> int:
        return hash (self._columns)

    def is_full(self):
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_matrix (self):
        return list(map(lambda column: column._line, self._columns))

    def add (self, char, col):
        if char == 'x' or char == 'o': 
            self._columns[col].add(char)

    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    
#------------------- Logica para detectar la victoria de un jugador ------------------    
    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result
    
    def _any_horizontal_victory(self, char):
        transponse_matrix = transpose (self.as_matrix())
        print ('Transpuesta:')
        print(transponse_matrix)
        aux_board = SquareBoard.fromList(transponse_matrix) 
        return aux_board._any_vertical_victory (char)
    
    def _any_sinking_victory (self, char):
        m = self.as_matrix()
        dm = displace_matrix(m)
        print ('Desplazada:')
        print(dm)
        tmp = SquareBoard.fromList(dm)
        return tmp._any_horizontal_victory(char)
    
    def _any_rising_victory (self, char):
        m = self.as_matrix ()
        rm = reverse_matrix (m)
        print ('Reverso:')
        print (rm)
        tmp = SquareBoard.fromList (rm)
        return tmp._any_horizontal_victory (char)
