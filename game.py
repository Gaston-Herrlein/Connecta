import pyfiglet
from settings import RoundType, DifficultyLevel
from match import Match
from player import Player, HumanPlayer
from square_board import SquareBoard

class Game ():
    def __init__ (self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player('Player_1'), Player('Player_2'))) -> None:
        self.round_type = round_type
        self.match = match
        self.board = SquareBoard ()


    def start (self):
        self.print_logo()
        self._configure_by_user()
        self._start_game_loop ()

    def print_logo(self):
        logo = pyfiglet.Figlet (font = 'stop')
        print(logo.renderText('Connecta'))

    def _configure_by_user (self):
        self._get_round_type()
        self.match = self._make_match()

    def _get_round_type (self):
        print ('SELECT TYPE OF ROUND: ')
        print ('1) COMPUTER VS COMPUTER')
        print ('2) COMPUTER VS HUMAN')

        response = ""
        while response != "1" and response != "2":
            response = input ('PLEASE TYPE EITHER 1 OR 2')
        
        if response == "1":
            self.round_type = RoundType.COMPUTER_VS_COMPUTER
        else:
            self.round_type = RoundType.COMPUTER_VS_HUMAN
        
    def _make_match(self):
        """
        El PLayer 1 sera siempre robot
        """
        player1 = Player ('Player1')
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player2 = Player ('Player2')
        else:
            player2 = HumanPlayer (name = input ('Enter your name: '))
        
        return Match (player1, player2)
    
    def _start_game_loop (self):
        """
        Bucle infinito... Obtengo el jugador de turno, le hago jugar, muestro su jugada e imprimo el tablero.
        Finalmente evaluo la condicion del juego (sigo en bucle o GAME OVER)
        """
        while True:
            current_player = self.match.next_player
            current_player.play (self.board)
            
            self.display_move ()
            self.display_board ()

            if self._is_game_over ():
                self.display_result ()
                break

    def _is_game_over (self):
        pass
    
    def display_move (self):
        pass

    def display_board (self):
        pass

    def display_result (self):
        pass