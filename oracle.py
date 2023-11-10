from square_board import SquareBoard
from settings import ColumnClassification

#Clase que alverga los metodos que nos recomiendan en que posicion jugar
class ColumnRecommendation ():
    def __init__ (self, index, classification):
        """
        Inicializador de la clase
        """
        self.index = index
        self.classification = classification

    def __repr__(self) -> str:
        """
        Dunder para representar la clase
        """
        return f'{self.__class__} index({self.index}), {self.classification}'
    
    def __eq__ (self, other):
        """
        Dunder necesario para comparar objetos de la misma clase
        """
        if not isinstance (other, self.__class__):
            return False
        return (self.index, self.classification) == (other.index, other.classification)
    
    def __hash__(self) -> int:
        """
        Dunder para obtener el hash del objeto/clase
        """
        return hash ((self.index, self.classification))
    
    def _set_classification(self, classification):
        """
        Establece la clasificacion enviada como parametro en el atributo de la clase
        """
        self.classification = classification

#Clase que sera el padre de los futuros oraculos mas 'inteligentes'
class BaseOracle ():
    def get_recommendation (self, board, player):
        """
        Establece una recomendacion para cada columna del tablero
        """
        recommendation = []
        for i in range(len(board)):
            recommendation.append(self._get_column_recommendation(board, i, player))
        return recommendation

    def _get_column_recommendation (self, board, i, player):
        """
        Originalmente clasifica la columna como MAYBE ('quizas sea buena idea jugar aquí').
        Si la columna esta llena se cambia a FULL ('no se puede jugar aquí')
        """
        classification = ColumnRecommendation (i, ColumnClassification.MAYBE)
        if board._columns[i].is_full():
            classification._set_classification(ColumnClassification.FULL)
        return classification
