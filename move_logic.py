import Board, Cell, Piece, Enums

def move_pawn(cells, x, y, selectedPiece):
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

def move_bishop(cells, x, y, selectedPiece):
    collided = False
    sameCollided = False
    for i in range(1, 8):
        print("--------------------")
        print (y + i)
        if((y+i) in range(8) and (x+i) in range(8) and cells[y+i][x+i].pieceInCell != None and cells[y+i][x+i].pieceInCell.color == selectedPiece.color):
            break
        if((y+i) in range(8) and (x+i) in range(8) and cells[y+i][x+i].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y+i][x+i])
        if((y+i) in range(8) and (x+i) in range(8) and cells[y+i][x+i].pieceInCell != None and cells[y+i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
            Board.board.possibleMoves.append(cells[y+i][x+i])
            collided = True
    collided = False
    for i in range(1, 8):
        if((y+i) in range(8) and (x-i) in range(8) and cells[y+i][x-i].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y+i][x-i])
        if((y+i) in range(8) and (x-i) in range(8) and cells[y+i][x-i].pieceInCell != None and cells[y+i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
            Board.board.possibleMoves.append(cells[y+i][x-i])
            collided = True
        if((y+i) in range(8) and (x-i) in range(8) and cells[y+i][x-i].pieceInCell != None and cells[y+i][x-i].pieceInCell.color == selectedPiece.color):
            break
    collided = False

    for i in range(1, 8):
        if((y-i) in range(8) and (x+i) in range(8) and cells[y-i][x+i].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y-i][x+i])
        if((y-i) in range(8) and (x+i) in range(8) and cells[y-i][x+i].pieceInCell != None and cells[y-i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
            Board.board.possibleMoves.append(cells[y-i][x+i])
            collided = True
        if((y-i) in range(8) and (x+i) in range(8) and cells[y-i][x+i].pieceInCell != None and cells[y-i][x+i].pieceInCell.color == selectedPiece.color):
            break
    collided = False
    for i in range(1, 8):
        if((y-i) in range(8) and (x-i) in range(8) and cells[y-i][x-i].pieceInCell == None):
            Board.board.possibleMoves.append(cells[y-i][x-i])
        if((y-i) in range(8) and (x-i) in range(8) and cells[y-i][x-i].pieceInCell != None and cells[y-i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
            Board.board.possibleMoves.append(cells[y-i][x-i])
            collided = True
        if((y-i) in range(8) and (x-i) in range(8) and cells[y-i][x-i].pieceInCell != None and cells[y-i][x-i].pieceInCell.color == selectedPiece.color):
            break
    
def move_king(cells, x, y, selectedPiece):
    print("pawn")

def move_queen(cells, x, y, selectedPiece):
    print("pawn")

def move_rook(cells, x, y, selectedPiece):
    print("pawn")

def move_knight(cells, x, y, selectedPiece):
    print("pawn")


moves = {
    Enums.PieceType.PAWN : move_pawn,
    Enums.PieceType.BISHOP : move_bishop,
    Enums.PieceType.KING : move_king,
    Enums.PieceType.QUEEN : move_queen,
    Enums.PieceType.KNIGHT : move_knight,
    Enums.PieceType.ROOK : move_rook
}