import Board, Cell, Piece, Enums

def move_pawn(cells, x, y):
    if(cells[y][x].pieceInCell.color == Enums.Color.BLACK):
        if(y == 1 and cells[y+2][x].pieceInCell == None and cells[y+1][x].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y+2][x])
        if((y+1)in range(8) and (x-1) in range(8) and cells[y+1][x-1].pieceInCell != None and cells[y+1][x-1].pieceInCell.color == Enums.Color.WHITE):
            Board.board.possibleMoves.append(cells[y+1][x-1])
        if((y+1)in range(8) and (x+1) in range(8) and cells[y+1][x+1].pieceInCell != None and cells[y+1][x+1].pieceInCell.color == Enums.Color.WHITE):
            Board.board.possibleMoves.append(cells[y+1][x+1])
        if((y+1) in range (8) and cells[y+1][x].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y+1][x])

    else:
        if(y == 6 and cells[y-2][x].pieceInCell == None and cells[y-1][x].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y-2][x])
        if((y-1)in range(8) and (x-1) in range(8) and cells[y-1][x-1].pieceInCell != None and cells[y-1][x-1].pieceInCell.color == Enums.Color.BLACK):
            Board.board.possibleMoves.append(cells[y-1][x-1])
        if((y-1)in range(8) and (x+1) in range(8) and cells[y-1][x+1].pieceInCell != None and cells[y-1][x+1].pieceInCell.color == Enums.Color.BLACK):
            Board.board.possibleMoves.append(cells[y-1][x+1])
        if((y-1) in range (8) and cells[y-1][x].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y-1][x])

def move_bishop(cells, x, y):
    print("bishop")

    
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