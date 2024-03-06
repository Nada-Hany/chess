import Enums

def ValidHorizontal(x, y, selectedPiece, board):
    collided = False
    for i in range(1, 8):
        if((x-i) in range(8)):
            if(board.cells[y][x-i].pieceInCell != None):
                if(board.cells[y][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y][x-i].pieceInCell.color != selectedPiece.color and (not collided)):
                    selectedPiece.possibleMoves.append(board.cells[y][x-i])
                    collided = True
            elif(board.cells[y][x-i].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(board.cells[y][x-i])
    collided = False
    for i in range(1, 8):
        if((x+i) in range(8)):
            if(board.cells[y][x+i].pieceInCell != None):
                if(board.cells[y][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y][x+i].pieceInCell.color != selectedPiece.color and (not collided)):
                    selectedPiece.possibleMoves.append(board.cells[y][x+i])
                    collided = True
            elif(board.cells[y][x+i].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(board.cells[y][x+i])

def ValidVertical(x, y, selectedPiece, board):
    collided = False
    for i in range(1, 8):
        if((y+i) in range(8)):
            if(board.cells[y+i][x].pieceInCell != None):
                if(board.cells[y+i][x].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y+i][x].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y+i][x])
                    collided = True
            elif(board.cells[y+i][x].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(board.cells[y+i][x])
    collided = False
    for i in range(1, 8):
           if((y-i) in range(8)):
            if(board.cells[y-i][x].pieceInCell != None):
                if(board.cells[y-i][x].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y-i][x].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y-i][x])
                    collided = True
            elif(board.cells[y-i][x].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(board.cells[y-i][x])

def CheckPrimalDiagonal(x, y, selectedPiece, board):
    collided = False
    for i in range(1,8):
        if((y+i) in range(8) and (x+i) in range(8)):
            if(board.cells[y+i][x+i].pieceInCell != None):
                if(board.cells[y+i][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y+i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y+i][x+i])
                    collided = True
            elif(board.cells[y+i][x+i].pieceInCell == None and (not collided)):
                    selectedPiece.possibleMoves.append(board.cells[y+i][x+i])
    collided = False
    for i in range(1,8):
        if((y-i) in range(8) and (x-i) in range(8)):
            if(board.cells[y-i][x-i].pieceInCell != None):
                if(board.cells[y-i][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y-i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y-i][x-i])
                    collided = True
            elif(board.cells[y-i][x-i].pieceInCell == None and (not collided)):
                    selectedPiece.possibleMoves.append(board.cells[y-i][x-i])

def CheckSecondaryDiagonal(x, y, selectedPiece, board):
    collided = False
    for i in range(1, 8):
        if((y+i) in range(8) and (x-i) in range(8)):
            if(board.cells[y+i][x-i].pieceInCell != None):
                if(board.cells[y+i][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y+i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y+i][x-i])
                    collided = True
            elif(board.cells[y+i][x-i].pieceInCell == None and not collided):
                    selectedPiece.possibleMoves.append(board.cells[y+i][x-i])
    collided = False
    for i in range(1, 8):
        if((y-i) in range(8) and (x+i) in range(8)):
            if(board.cells[y-i][x+i].pieceInCell != None):
                if(board.cells[y-i][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(board.cells[y-i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(board.cells[y-i][x+i])
                    collided = True
            elif(board.cells[y-i][x+i].pieceInCell == None and not collided):
                    selectedPiece.possibleMoves.append(board.cells[y-i][x+i])

def CheckDiagonally(x, y, selectedPiece, board):
    CheckSecondaryDiagonal(x, y, selectedPiece, board)
    CheckPrimalDiagonal(x, y, selectedPiece, board)

def move_pawn(x, y, selectedPiece, board):
    if(board.cells[y][x].pieceInCell.color == Enums.Color.BLACK):
        if(y == 1 and board.cells[y+2][x].pieceInCell == None and board.cells[y+1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+2][x])
        if((y+1)in range(8) and (x-1) in range(8) and board.cells[y+1][x-1].pieceInCell != None and
           board.cells[y+1][x-1].pieceInCell.color == Enums.Color.WHITE):
            selectedPiece.possibleMoves.append(board.cells[y+1][x-1])
        if((y+1)in range(8) and (x+1) in range(8) and board.cells[y+1][x+1].pieceInCell != None and 
           board.cells[y+1][x+1].pieceInCell.color == Enums.Color.WHITE):
            selectedPiece.possibleMoves.append(board.cells[y+1][x+1])
        if((y+1) in range (8) and board.cells[y+1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+1][x])

    else:
        if(y == 6 and board.cells[y-2][x].pieceInCell == None and board.cells[y-1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-2][x])
        if((y-1)in range(8) and (x-1) in range(8) and board.cells[y-1][x-1].pieceInCell != None and 
           board.cells[y-1][x-1].pieceInCell.color == Enums.Color.BLACK):
            selectedPiece.possibleMoves.append(board.cells[y-1][x-1])
        if((y-1)in range(8) and (x+1) in range(8) and board.cells[y-1][x+1].pieceInCell != None and 
           board.cells[y-1][x+1].pieceInCell.color == Enums.Color.BLACK):
            selectedPiece.possibleMoves.append(board.cells[y-1][x+1])
        if((y-1) in range (8) and board.cells[y-1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-1][x])

def move_bishop(x, y, selectedPiece, board):
    CheckDiagonally(x, y, selectedPiece, board)

def move_king(x, y, selectedPiece, board):
    if((y-1)in range(8) and (x+1) in range(8) and board.cells[y-1][x+1].pieceInCell != None and 
       board.cells[y-1][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y-1][x+1])
    if((y+1)in range(8) and (x+1) in range(8) and board.cells[y+1][x+1].pieceInCell != None and 
       board.cells[y+1][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y+1][x+1])
    if((y+1)in range(8) and (x-1) in range(8) and board.cells[y+1][x-1].pieceInCell != None and 
       board.cells[y+1][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y+1][x-1])
    if((y-1)in range(8) and (x-1) in range(8) and board.cells[y-1][x-1].pieceInCell != None and 
       board.cells[y-1][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y-1][x-1])

    if((y-1)in range(8) and board.cells[y-1][x].pieceInCell != None and
        board.cells[y-1][x].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y-1][x])
    if((y+1)in range(8) and board.cells[y+1][x].pieceInCell != None and
        board.cells[y+1][x].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y+1][x])
    if((x-1) in range(8) and board.cells[y][x-1].pieceInCell != None and 
       board.cells[y][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y][x-1])
    if((x+1) in range(8) and board.cells[y][x+1].pieceInCell != None and
        board.cells[y][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(board.cells[y][x+1])

    if((y+1) in range (8) and board.cells[y+1][x].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y+1][x])
    if((y-1) in range (8) and board.cells[y-1][x].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y-1][x])
    if((x+1) in range (8) and board.cells[y][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y][x+1])
    if((x-1) in range (8) and board.cells[y][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y][x-1])

    if((y+1) in range (8) and (x+1) in range(8) and board.cells[y+1][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y+1][x+1])
    if((y-1) in range (8) and (x-1) in range(8) and board.cells[y-1][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y-1][x-1])
    if((y-1) in range(8) and (x+1) in range (8) and board.cells[y-1][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y-1][x+1])
    if((y+1) in range(8) and (x-1) in range (8) and board.cells[y+1][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(board.cells[y+1][x-1])

def move_queen(x, y, selectedPiece, board):
    ValidHorizontal(x, y, selectedPiece, board)
    CheckDiagonally(x, y, selectedPiece, board)
    ValidVertical(x, y, selectedPiece, board)

def move_rook(x, y, selectedPiece, board):
    ValidHorizontal(x, y, selectedPiece, board)
    ValidVertical(x, y, selectedPiece, board)

def move_knight(x, y, selectedPiece, board):
    if((y-2) in range(8) and (x+1) in range(8)):
        if(board.cells[y-2][x+1].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-2][x+1])
        else:
            if(board.cells[y-2][x+1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y-2][x+1])

    if((y-2) in range(8) and (x-1) in range(8)):
        if(board.cells[y-2][x-1].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-2][x-1])
        else:
            if(board.cells[y-2][x-1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y-2][x-1])

    if((y+2) in range(8) and (x+1) in range(8)):
        if(board.cells[y+2][x+1].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+2][x+1])
        else:
            if(board.cells[y+2][x+1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y+2][x+1])

    if((y+2) in range(8) and (x-1) in range(8)):
        if(board.cells[y+2][x-1].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+2][x-1])
        else:
            if(board.cells[y+2][x-1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y+2][x-1])

    
    if((y+1) in range(8) and (x-2) in range(8)):
        if(board.cells[y+1][x-2].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+1][x-2])
        else:
            if(board.cells[y+1][x-2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y+1][x-2])
    
    if((y-1) in range(8) and (x+2) in range(8)):
        if(board.cells[y-1][x+2].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-1][x+2])
        else:
            if(board.cells[y-1][x+2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y-1][x+2])
    
    if((y-1) in range(8) and (x-2) in range(8)):
        if(board.cells[y-1][x-2].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y-1][x-2])
        else:
            if(board.cells[y-1][x-2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y-1][x-2])


    if((y+1) in range(8) and (x+2) in range(8)):
        if(board.cells[y+1][x+2].pieceInCell == None):
            selectedPiece.possibleMoves.append(board.cells[y+1][x+2])
        else:
            if(board.cells[y+1][x+2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(board.cells[y+1][x+2])
                    
moves = {
    Enums.PieceType.PAWN : move_pawn,
    Enums.PieceType.BISHOP : move_bishop,
    Enums.PieceType.KING : move_king,
    Enums.PieceType.QUEEN : move_queen,
    Enums.PieceType.KNIGHT : move_knight,
    Enums.PieceType.ROOK : move_rook
}