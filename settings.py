from enum import Enum, auto

BOARD_LENGTH = 4
VICTORY_STRICK = 3

class ColumnClassification (Enum):
    MAYBE = auto()
    FULL = auto()