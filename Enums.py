from enum import Enum 

class Color(Enum):
    BLACK = 0
    WHITE = 1

class GameState(Enum):
    PAUSED = 0
    RUNNING = 1
    GAME_OVER = 2
    BLACK_WON = 3
    WHITE_WON = 4

class PieceType(Enum):
    BISHOP = 0 
    KING = 1 
    QUEEN = 2
    PAWN = 3
    KNIGHT = 4
    ROOK = 5