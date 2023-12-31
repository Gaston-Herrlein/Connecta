import pyfiglet
from settings import BOARD_LENGTH, RoundType, DifficultyLevel
from match import Match
from player import Player, ReportingPlayer, HumanPlayer
from square_board import SquareBoard
from list_utils import reverse_matrix
from beautifultable import BeautifulTable
from oracle import BaseOracle, SmartOracle, LearningOracle


class Game:
    def __init__(
        self,
        round_type=RoundType.COMPUTER_VS_COMPUTER,
        match=Match(Player("Player_1"), Player("Player_2")),
    ) -> None:
        """
        Inicializamos la clase con valores preestablecidos que posteriormente podra modificar el jugador
        """
        self.round_type = round_type
        self.match = match
        self.board = SquareBoard()

    def start(self):
        """
        Metodo que inicializa el juego.
        Primero imprime el logo
        Segundo configura la partida el usuario
        Tercero iniciamos el loop principal del juego
        """
        self.print_logo()
        self._configure_by_user()
        self._start_game_loop()

    def print_logo(self):
        """
        Metodo que utiliza la libreria 'pyfiglet' para imprimir el logo
        """
        logo = pyfiglet.Figlet(font="stop")
        print(logo.renderText("Connecta"))

    def _configure_by_user(self):
        """
        Metodo que configura la partida segun preferencias del usuario
        Primero se configura el tipo de partida
        Segundo, si la partida es PC vs Humano, se le pregunta al usuario nivel de dificultad
        Tercero se configura la instancia match segun lo que haya elegido el usuario
        """
        self._set_round_type()
        if self.round_type == RoundType.COMPUTER_VS_HUMAN:
            self._difficulty_level = self._get_difficulty_level()
        self.match = self._make_match()

    def _set_round_type(self):
        """
        Selecciona el tipo de partida CPU-CPU o CPU-Humano.
        Este metodo modifica directamente el atriburo 'round_type'
        """

        print(
            """
        SELECT TYPE OF ROUND:
        1) COMPUTER VS COMPUTER
        2) COMPUTER VS HUMAN
        """
        )

        response = ""
        while response != "1" and response != "2":
            response = input("PLEASE TYPE EITHER 1 OR 2 \n\t")

        if response == "1":
            self.round_type = RoundType.COMPUTER_VS_COMPUTER
        else:
            self.round_type = RoundType.COMPUTER_VS_HUMAN

    def _make_match(self):
        """
        Metodo que define el player 2 segun haya que haya elegido el jugador en el metodo '_get_round_typy()'
        El Player 1 sera siempre robot.
        Este metodo retorna la partida (match) con los jugadores pertinentes
        """
        _levels = {
            DifficultyLevel.LOW: BaseOracle(),
            DifficultyLevel.MEDIUM: SmartOracle(),
            DifficultyLevel.HARD: LearningOracle(),
        }

        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = ReportingPlayer("Rick", oracle=_levels[DifficultyLevel.HARD])
            player2 = Player("Morty")
        else:
            player1 = Player("Rick", oracle=_levels[self._difficulty_level])
            player2 = HumanPlayer(name=input("Enter your name: "))

        return Match(player1, player2)

    def _start_game_loop(self):
        """
        Bucle infinito... Obtengo el jugador de turno, le hago jugar, muestro su jugada e imprimo el tablero.
        Finalmente evaluo la condicion del juego (sigo en bucle o GAME OVER)
        """
        while True:
            current_player = self.match.next_player
            current_player.play(self.board)

            self.display_move(current_player)
            self.display_board()

            if self.has_winner_or_tie():
                self.display_result()

                if self.match.is_match_over():
                    break
                else:
                    self.board = SquareBoard()
                    self.display_board()

    def has_winner_or_tie(self):
        """
        El juego termina cuando hay un empate (tablero lleno) o cuando hay un ganador
        """
        is_game_over = False
        winner = self.match.get_winner(self.board)
        if winner != None:
            winner.on_win()
            winner.opponent.on_lose()
            is_game_over = True
        elif self.board.is_full():
            is_game_over = True
        return is_game_over

    def display_move(self, player):
        """
        Muestra por pantalla el ultimo movimiento
        """
        print(
            f"\n{player.name} ({player.char}) has moved in column #{player.last_moves[0].position}\n"
        )

    def display_board(self):
        """
        Muestra por pantalla el tablero actual
        """
        matrix = self.board.as_matrix()
        matrix = reverse_matrix(matrix)

        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        print(bt)

    def display_result(self):
        """
        Muestra por pantalla el resultado de la partida
        """
        winner = self.match.get_winner(self.board)
        if winner != None:
            print(f"\n{winner.name} ({winner.char}) wins!!!")
        else:
            print(
                f'\nA tie between {self.match.get_player("x").name} (x) and {self.match.get_player("o").name} (o)!'
            )

    def _get_difficulty_level(self):
        """
        Pregunta al usuario nivel de dificultad para configurar el oraculo
        """
        print(
            """
        Chose your opponent:
        1) Bender (easy)
        2) T-800 (medium)
        3) T-3000 (hard)
        """
        )
        level = DifficultyLevel.LOW
        while True:
            response = input("Please type 1, 2 or 3: ")
            if response == "1":
                level = DifficultyLevel.LOW
                break
            elif response == "2":
                level = DifficultyLevel.MEDIUM
                break
            elif response == "3":
                level = DifficultyLevel.HARD
                break
            else:
                print("Please into to 1, 2 or 3\n")
        return level
