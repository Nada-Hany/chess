import Board, Cell, Piece, Enums

def move_bishop(cells, x, y):
    print("bishop")

def move_pawn(cells, x, y):
    print("pawn")
    
def move_king(cells, x, y):
    print("pawn")

def move_queen(cells, x, y):
    print("pawn")

def move_rook(cells, x, y):
    print("pawn")

def move_knight(cells, x, y):
    print("pawn")


moves = {
    Enums.PieceType.PAWN : move_pawn,
    Enums.PieceType.BISHOP : move_bishop,
    Enums.PieceType.KING : move_king,
    Enums.PieceType.QUEEN : move_queen,
    Enums.PieceType.KNIGHT : move_knight,
    Enums.PieceType.ROOK : move_rook
}