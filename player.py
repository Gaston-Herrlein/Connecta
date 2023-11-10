from oracle import BaseOracle, ColumnRecommendation
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
    """
    Juega en un tablero despues de preguntarle al oraculo
    """
    def __init__(self, name, char = None, opponent = None,  oracle = BaseOracle()) -> None:
        """
        Inicializamos el jugador, por defecto los parametros estan vacios y el oraculo es BaseOracule 
        para posteriormente modificarlo
        """
        self.name = name
        self.char = char
        self.opponent = opponent
        self._oracle = oracle

    @property
    def opponent (self):
        return self._opponent
    
    @opponent.setter
    def opponent (self, other):
        if other != None:
            self._opponent = other
            other._opponent = self

    def __repr__(self) -> str:
        return f'{self.name}'

    def play (self, board):
        """
        Primero le pregunta al oraculo. Guarda una tupla con la mejor opción para jugar y todas las recomendaciones
        Segundo procede a realizar la jugada
        """
        (best, recommendation) = self._ask_oracle (board)
        self._play_on (board, best.index)
    
    def _play_on (self, board, index):
        """
        Metodo para realizar la jugada
        """
        board.add (self.char, index)

    def _ask_oracle (self, board):
        """
        Metodo para preguntarle al oraculo.
        Este metodo devuelve 2 parametros, en primer lugar la mejor opcion para jugar y 
        segundo una lista con todas la recomendaciones por cada columna del tablero
        """
        recommendation = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendation)
        return (best, recommendation)

    def _choose (self, recommendations):
        """
        Metodo para determinar cual es la mejor opcion. 
        En primera instancia devuelve el primer valor que encuentra con la recomendaión distinta de FULL.
        Posteriormente este metodo se sobreescribira para una respuesta mas util
        """
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
        return valid[0]

#Clase que hereda de Player y se utilizara con los jugadores humanos
class HumanPlayer (Player):
    def __init__ (self, name, char = None):
        super.__init__(name, char)
    
    def _ask_oracle (self, board):
        """
        Para el caso del jugador humano le preguntamos en que columna quiere jugar.
        Si la columna solicitada no esta llena procede a jugar
        """
        while True:
            raw = input ("Selecciona una columna: ")
            validation = _is_int(raw) and _is_within_column_range (int(raw)) and _is_non_full_column (int(raw))
            if validation:
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)
            