from settings import BOARD_LENGTH, VICTORY_STRICK
from list_utils import find_streak

class  LinearBoard():

    @classmethod
    def fromList(cls, list):
        """
        Metodo de clase que permite armar un LinearBoard sin instanciar la clase
        """
        column = cls()
        if len(list) <= BOARD_LENGTH:    
            column._line = list
        return column

    def __init__ ( self ):
        """
        Inicializamos la clase con una lista de longitud 'BOARD_LENGTH' pero vacia ('None')
        """
        self._line = []
        for i in range(BOARD_LENGTH):
            self._line.append (None)
            

    def __eq__ (self, other):
        """
        Metodo especial (dunder), que nos permite igualar dos objetos de la misma clase 
        """
        if not isinstance (other, self.__class__):
            return False
        else:
            return self._line == other._line
        
    def __hash__(self) -> int:
        """
        Dunder necesario y complemetario que van 'de la mano' con __eq__
        """
        return hash (self._line)

    def __repr__(self) -> str:
        """
        Dunder para representar un LinearBoard
        """
        return f'{self._line}'    

    def is_full (self):
        """
        Metodo que sirve para saber si una LinearBoard esta completa o no"""
        line_aux = list(filter(lambda x: x != None, self._line))
        if len(line_aux) == BOARD_LENGTH:
            return True
        return False

    def is_victory (self, x):
        """
        Metodo que recibe un caracter y evalua si hay una victoria de ese caracter
        """
        return find_streak (self._line, x)

    def add (self, char):
        """
        Metodo que agrega el caracter que se le envia como parametro al LinearBoard
        """
        if not self.is_full():
            i = self._line.index(None)
            self._line[i] = char

    def is_tie ( self, x, o):
        """
        Metodo que a partir de dos caracteres que toma como parametro, nos indica si hay empate
        Para esto utilizamos una funcion de list_utils (find_streake()) para saber si hay una racha de VICTORY_STRIKE 
        """
        tie = False
        if not find_streak (self._line, x) and not find_streak (self._line, o):
            tie = True
        return tie


