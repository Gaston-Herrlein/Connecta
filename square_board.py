from linear_board import LinearBoard
from list_utils import transpose, displace_matrix, reverse_matrix
from settings import BOARD_LENGTH

class SquareBoard ():

    @classmethod
    def fromList(cls, list_of_lists):
        """
        Metodo de clase para armar un tablero sin instanciar la clase
        """
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_lists))
        return board

    def __init__ (self):
        """
        Dunder para inicializar la clase. Inicializamos el tablero creando 'n' (BOARD_LENGTH) 'LinearBoard'
        """
        self._columns = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def __repr__ (self):
        """
        Dunder para representar el tablero
        """
        return f'{self.__class__}: {self._columns}'
    
    def __len__ (self):
        """
        Dunder que nos indica la cantidad de columnas del tablero
        """
        return len (self._columns)
    
    def __eq__ (self, other):
        """
        Dunder que nos sirve para realizar comparaciones entre dos objetos de la misma clase
        """
        if not isinstance (other, self.__class__):
            return False
        else:
            return self._columns == other._columns
        
    def __hash__(self) -> int:
        """
        Dunder para obtener el hash de nuestro clase/objeto"""
        return hash (self._columns)

    def is_full(self):
        """
        Metodo que recorre el tablero (matriz) y devuelve True/False segun este lleno o no
        """
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_matrix (self):
        """
        Representa el trablero como una lista de listas, en lugar de una lista de LinearBoard"""
        return list(map(lambda column: column._line, self._columns))

    def add (self, char, col):
        """
        Metodo que sirve para agregar un caracter, recibido como parametro, en una columna, tambien recibida como parametro
        """
        if char == 'x' or char == 'o': 
            self._columns[col].add(char)

    def is_victory(self, char):
        """
        Metodo que agrupa varios metodos con los cuales se comprueba cada caso de victoria (vertical, horizontal, diagonal asc o diagonal desc)
        """
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or self._any_sinking_victory(char)

    
#------------------- Logica para detectar la victoria de un jugador ------------------    
    def _any_vertical_victory(self, char):
        """
        Metodo que devuelve True/False segun haya una victoria vertical del caracter recibido como parametro
        """
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result
    
    def _any_horizontal_victory(self, char):
        """
        Metodo que devuelve True/False segun haya una victoria horizontal
        Para esto transpone la matriz original (tablero) y llama a la funcion '_any_vertical_victory()'
        """
        transponse_matrix = transpose (self.as_matrix())
        aux_board = SquareBoard.fromList(transponse_matrix) 
        return aux_board._any_vertical_victory (char)
    
    def _any_sinking_victory (self, char):
        """
        Metodo que devuelve True/False segun haya una victoria diagonal asc
        Para esto desplaza 'n' lugares la 'enecima columnas' de la matriz original (tablero) y llama a la funcion '_any_horizontal_victory()'
        """
        m = self.as_matrix()
        dm = displace_matrix(m)
        tmp = SquareBoard.fromList(dm)
        return tmp._any_horizontal_victory(char)
    
    def _any_rising_victory (self, char):
        """
        Metodo que devuelve True/False segun haya una victoria diagonal desc
        Para esto desplaza 'n' lugares la 'enecima columnas' de la matriz original (tablero) para posteriormente revertirla y
        finalmente llama a la funcion '_any_sinking_victory()
        """
        m = self.as_matrix ()
        rm = reverse_matrix (m)
        tmp = SquareBoard.fromList (rm)
        return tmp._any_sinking_victory (char)
