from beautifultable import BeautifulTable
from oracle import SmartOracle, ColumnRecommendation
from settings import ColumnClassification, BOARD_LENGTH
from list_utils import all_same
from move import Move
import random


def _is_within_column_range(col):
    return col >= 0 and col < BOARD_LENGTH


def _is_non_full_column(board, col):
    return not board._columns[col].is_full()


def _is_int(col):
    try:
        nume = int(col)
        return True
    except:
        return False


class Player:
    def __init__(self, name, char=None, opponent=None, oracle=SmartOracle()) -> None:
        """
        Inicializamos el jugador, por defecto los parametros estan vacios y el oraculo es BaseOracule
        para posteriormente modificarlo
        """
        self.name = name
        self.char = char
        self.opponent = opponent
        self._oracle = oracle
        self.last_moves = None  # Se define como 'None' ya que posteriormente se guarda una clase con el ultimo mov

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, other):
        if other != None:
            self._opponent = other
            other._opponent = self

    def __repr__(self) -> str:
        return f"{self.name}"

    def play(self, board):
        """
        Primero le pregunta al oraculo. Guarda una tupla con la mejor opción para jugar y todas las recomendaciones
        Segundo procede a realizar la jugada
        """
        (best, recommendations) = self._ask_oracle(board)
        self._play_on(board, best.index, recommendations)

    def _play_on(self, board, index, recommendations):
        """
        Juega en la columna 'index'.
        Guardar la ultima jugada, que se utilizara para 'aprender de los errores'
        """
        board.add(self.char, index)
        self.last_moves = Move(index, board.as_code(), recommendations, self)

    def _ask_oracle(self, board):
        """
        Este metodo devuelve un tupla, en primer lugar la mejor opcion para jugar y
        segundo una lista con todas la recomendaciones.
        """
        recommendation = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendation)
        return (best, recommendation)

    def _choose(self, recommendations):
        """
        Determinar cual es la mejor opcion.
        """
        valid = list(
            filter(
                lambda x: x.classification != ColumnClassification.FULL, recommendations
            )
        )
        # Ordeno la lista
        valid.sort(key=lambda x: x.classification.value, reverse=True)
        if all_same(valid):
            return random.choice(valid)
        else:
            return valid[0]

    def display_recommendations(self, board):
        recs = map(
            lambda x: str(x.classification).split(".")[1].lower(),
            self._oracle.get_recommendation(board, self),
        )

        bt = BeautifulTable()
        bt.rows.append(recs)

        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]

        print(bt)


# Clase que hereda de Player y se utilizara con los jugadores humanos
class HumanPlayer(Player):
    def __init__(self, name, char=None):
        super().__init__(name, char)

    def _ask_oracle(self, board):
        """
        Le pregunta al jugador en que columna quiere jugar.
        Si la columna solicitada no esta llena procede a jugar
        """
        while True:
            raw = input("Selecciona una columna (o 'h' para ver las recomendaciones): ")
            validation = (
                _is_int(raw)
                and _is_within_column_range(int(raw))
                and _is_non_full_column(board, int(raw))
            )
            if validation:
                pos = int(raw)
                return (ColumnRecommendation(pos, None), None)

            elif raw == "h":
                self.display_recommendations(board)

    def on_win(self):
        pass

    def on_lose(self):
        pass


class ReportingPlayer(Player):
    def on_lose(self):
        """
        Actualiza la ultima recomendacion del oraculo
        """
        board_code = self.last_moves.board_code
        position = self.last_moves.position
        self._oracle.update_to_bad(board_code, self, position)
