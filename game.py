import pyfiglet
from settings import RoundType
from match import Match
from player import Player, HumanPlayer
from square_board import SquareBoard

class Game ():
    def __init__ (self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player('Player_1'), Player('Player_2'))) -> None:
        """
        Inicializamos la clase con valores preestablecidos que posteriormente podra modificar el jugador
        """
        self.round_type = round_type
        self.match = match
        self.board = SquareBoard ()


    def start (self):
        """
        Metodo que inicializa el juego. 
        Primero imprime el logo
        Segundo configura la partida el usuario
        Tercero iniciamos el loop principal del juego
        """
        self.print_logo()
        self._configure_by_user()
        self._start_game_loop ()

    def print_logo(self):
        """
        Metodo que utiliza la libreria 'pyfiglet' para imprimir el logo
        """
        logo = pyfiglet.Figlet (font = 'stop')
        print(logo.renderText('Connecta'))

    def _configure_by_user (self):
        """
        Metodo que configura la partida segun preferencias del usuario
        Primero se configura el tipo de partida
        Segundo se configura la instancia match segun lo que haya elegido el usuario
        """
        self._set_round_type()
        self.match = self._make_match()

    def _set_round_type (self):
        """
        Selecciona el tipo de partida CPU-CPU o CPU-Humano.
        Este metodo modifica directamente el atriburo 'round_type'
        """
        
        print ("""
        SELECT TYPE OF ROUND:
        1) COMPUTER VS COMPUTER')
        2) COMPUTER VS HUMAN
        """)

        response = ""
        while response != "1" and response != "2":
            response = input ('PLEASE TYPE EITHER 1 OR 2')
        
        if response == "1":
            self.round_type = RoundType.COMPUTER_VS_COMPUTER
        else:
            self.round_type = RoundType.COMPUTER_VS_HUMAN
        
    def _make_match(self):
        """
        Metodo que define el player 2 segun haya que haya elegido el jugador en el metodo '_get_round_typy()'
        El PLayer 1 sera siempre robot.
        Este metodo retorna la partida (match) con los jugadores pertinentes
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