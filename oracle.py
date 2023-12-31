from square_board import SquareBoard
from settings import ColumnClassification
from copy import deepcopy


# Clase que alverga los metodos que nos recomiendan en que posicion jugar
class ColumnRecommendation:
    def __init__(self, index, classification):
        self.index = index
        self.classification = classification

    def __repr__(self) -> str:
        return f"{self.__class__} index({self.index}), {self.classification}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.classification == other.classification

    def __hash__(self) -> int:
        return hash(self.classification)

    def _set_classification(self, classification):
        """
        Establece la clasificacion enviada como parametro en el atributo de la clase
        """
        self.classification = classification


# Clase que sera el padre de los futuros oraculos mas 'inteligentes'
class BaseOracle:
    def get_recommendation(self, board, player):
        """
        Establece una recomendacion para cada columna del tablero
        """
        recommendation = []
        for i in range(len(board)):
            recommendation.append(self._get_column_recommendation(board, i, player))
        return recommendation

    def _get_column_recommendation(self, board, i, player):
        """
        Originalmente clasifica la columna como MAYBE ('quizas sea buena idea jugar aquí').
        Si la columna esta llena se cambia a FULL ('no se puede jugar aquí')
        """
        classification = ColumnRecommendation(i, ColumnClassification.MAYBE)
        if board._columns[i].is_full():
            classification._set_classification(ColumnClassification.FULL)
        return classification

    # Metodos para sobreescribie
    def update_to_bad(self, move):
        pass

    def backtrack(self, list_on_moves):
        pass


class SmartOracle(BaseOracle):
    def get_recommendation(self, board, player):
        return super().get_recommendation(board, player)

    def _get_column_recommendation(self, board, i, player):
        """
        Mejora la clasificaion dada por la clase 'BaseOracle'.
        Si originalmente la clasificaicon es 'MAYBE' comprobamos si hay un movimiento ganador o perdedor
        y reclasificamos(WIN, LOSE)
        """
        recommendation = super()._get_column_recommendation(board, i, player)
        if recommendation.classification == ColumnClassification.MAYBE:
            if self._is_winning_move(board, i, player):
                recommendation._set_classification(ColumnClassification.WIN)
            elif self._is_losing_move(board, i, player):
                recommendation._set_classification(ColumnClassification.LOSE)
        return recommendation

    def _is_winning_move(self, board, i, player):
        """
        Sobre una copia del tablero agrego la ficha en la columna indicada por parametro
        y compruebo si hay una victoria
        """
        flag = False
        board_copy = deepcopy(board)
        board_copy.add(player.char, i)
        if board_copy.is_victory(player.char):
            flag = True
        return flag

    def _is_losing_move(self, board, i, player):
        """
        Sobre una copia del tablero agrego la ficha, DEL OPONENTE, en la columna indicada por parametro
        y compruebo si hay una victoria DEL OPONENTE.
        """
        flag = False
        board_copy = deepcopy(board)
        board_copy.add(player.opponent.char, i)
        if board_copy.is_victory(player.opponent.char):
            flag = True
        return flag

    def no_good_options(self, board, player):
        """
        Analiza las recomendaciones y me devuelve un booleando
        que refleja si exite una buena opcion para jugar
        """
        recommendations = self.get_recommendation(board, player)

        is_everything_lost = recommendations.count(
            ColumnRecommendation(0, ColumnClassification.LOSE)
        )
        is_not_win = recommendations.count(
            ColumnRecommendation(0, ColumnClassification.WIN)
        )
        is_not_maybe = recommendations.count(
            ColumnRecommendation(0, ColumnClassification.MAYBE)
        )

        return (
            is_not_win != 0
            or is_everything_lost >= 2
            or (is_everything_lost == 1 and is_not_maybe == 0)
        )


class MemorizeOracle(SmartOracle):
    """
    Clase cuya funcionalidad es recordar todos los tableros y sus
    respectivas recomendaciones
    """

    def __init__(self) -> None:
        super().__init__()
        self._past_recommendations = {}

    def _make_key(self, board_code, player):
        """
        Metodo que guarda genera la clave para el diccionario que almacena las recomendaciones.
        Se tiene en cuenta el tablero (colapsado en un string) y el caracter del jugador
        """
        return f"{board_code.raw_code}@{player.char}"

    def get_recommendation(self, board, player):
        """
        Sobreescribimos get_recomendation para que memorice el tablero y la recomendacion
        """
        key = self._make_key(board.as_code(), player)

        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(board, player)
        return self._past_recommendations[key]


class LearningOracle(MemorizeOracle):
    def update_to_bad(self, move):
        key = self._make_key(move.board_code, move.player)
        recommendation = self.get_recommendation(
            SquareBoard.fromBoardCode(move.board_code._raw_code), move.player
        )
        recommendation[move.position] = ColumnRecommendation(
            move.position, ColumnClassification.BAD
        )

        self._past_recommendations[key] = recommendation

    def backtrack(self, list_on_moves):
        """
        Repasa todas las jugadas y si encuentra una en la que estaba todo perdido quiere
        decir que la anterior tiene que ser actualizada
        """
        for move in list_on_moves:
            self.update_to_bad(move)
            board = SquareBoard.fromBoardCode(move.board_code._raw_code)
            if not self.no_good_options(board, move.player):
                break
