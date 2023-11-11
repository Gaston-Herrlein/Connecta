from player import Player
from square_board import SquareBoard

class Match ():
    def __init__(self, player1, player2):
        """
        Inicializamos la clase asignandole los correspondientes caracteres y oponente a cada jugador
        Por simplicidad el player1 siempre sera 'x'
        """
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2

        self._players = {'x': player1, 'o': player2}
        self._round_robbin = [player1, player2]

    @property
    def next_player (self):
        """
        Propiedad de la clase que utilizaremos para saber los turnos de cada jugador.
        Devuelve el jugador al cual le corresponderia jugar
        """
        next_one = self._round_robbin[0]
        self._round_robbin.reverse()
        return next_one

    def get_player (self, char):
        """
        Devuelve el jugador con el caracter que se le envia como parametro
        """
        return self._players[char]
    
    def get_winner (self, board):
        """
        Dado un tablero, evalua que jugador (Player1 o Player2, resulta vencedor).
        En caso que no haya vencedor, devuelve None
        """
        if board.is_victory ('x'):
            return self.get_player ('x')
        
        elif board.is_victory ('o'):
            return self.get_player ('o')
        
        else:
            return None