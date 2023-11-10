from enum import Enum, auto

BOARD_LENGTH = 4
VICTORY_STRICK = 3

class ColumnClassification (Enum):
    MAYBE = auto()
    FULL = auto()

class RoundType (Enum):
    COMPUTER_VS_COMPUTER = auto ()
    COMPUTER_VS_HUMAN = auto ()

class DifficultyLevel (Enum):
    LOW = auto ()
    MEDIUM = auto ()
    HIGH = auto ()