from settings import BOARD_LENGTH
from list_utils import find_streak


class LinearBoard:
    @classmethod
    def fromList(cls, list):
        """
        Metodo de clase que permite armar un LinearBoard sin instanciar la clase
        """
        column = cls()
        if len(list) <= BOARD_LENGTH:
            column._line = list
        return column

    def __init__(self):
        """
        Inicializamos la clase con una lista de longitud 'BOARD_LENGTH' vacia ('None')
        """
        self._line = []
        for i in range(BOARD_LENGTH):
            self._line.append(None)

    def __eq__(self, other):
        """
        Dunder que nos permite igualar dos objetos de la misma clase
        """
        if not isinstance(other, self.__class__):
            return False
        else:
            return self._line == other._line

    def __hash__(self) -> int:
        """
        Dunder necesario y complemetario que van 'de la mano' con __eq__
        """
        return hash(self._line)

    def __repr__(self) -> str:
        """
        Dunder para representar un LinearBoard por consola
        """
        return f"{self._line}"

    def is_full(self):
        """
        Nos dice si el LinearBoard esta completa. Devuelve un Booleano
        """
        flag = False
        line_aux = list(filter(lambda x: x != None, self._line))
        if len(line_aux) == BOARD_LENGTH:
            flag = True
        return flag

    def is_victory(self, x):
        """
        Recibe un caracter y evalua si hay una victoria de ese caracter
        """
        return find_streak(self._line, x)

    def add(self, char):
        """
        Agrega el caracter que recibe como parametro
        """
        if not self.is_full():
            i = self._line.index(None)
            self._line[i] = char

    def is_tie(self, x, o):
        """
        Recibe dos caracteres y nos indica si hay empate
        """
        tie = False
        if not self.is_victory(x) and not self.is_victory(o):
            tie = True
        return tie
