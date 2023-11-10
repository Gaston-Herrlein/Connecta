from enum import Enum, auto

#Constantes preestablecidas para el largo del tablero
#Y el numero consecuentes de caracteres para una victoria
BOARD_LENGTH = 4
VICTORY_STRICK = 3

#Enumeracion que indica si conviene jugar en esa columna o esta llena (MAYBE, FULL respectivamente)
class ColumnClassification (Enum):
    MAYBE = auto()
    FULL = auto()

#Enumeracion que indica el tipo de partida
class RoundType (Enum):
    COMPUTER_VS_COMPUTER = auto ()
    COMPUTER_VS_HUMAN = auto ()

#Enumeracion que indica la dificultad de la partida
class DifficultyLevel (Enum):
    LOW = auto ()
    MEDIUM = auto ()
    HIGH = auto ()