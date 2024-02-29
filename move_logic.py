import Board, Enums

def CheckHorizontal(cells, x, y, selectedPiece):
    collided = False
    for i in range(1, 8):
        if((x-i) in range(8)):
            if(cells[y][x-i].pieceInCell != None):
                if(cells[y][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y][x-i].pieceInCell.color != selectedPiece.color and (not collided)):
                    selectedPiece.possibleMoves.append(cells[y][x-i])
                    collided = True
            elif(cells[y][x-i].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(cells[y][x-i])
    collided = False
    for i in range(1, 8):
        if((x+i) in range(8)):
            if(cells[y][x+i].pieceInCell != None):
                if(cells[y][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y][x+i].pieceInCell.color != selectedPiece.color and (not collided)):
                    selectedPiece.possibleMoves.append(cells[y][x+i])
                    collided = True
            elif(cells[y][x+i].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(cells[y][x+i])

def CheckVertical(cells, x, y, selectedPiece):
    collided = False
    for i in range(1, 8):
        if((y+i) in range(8)):
            if(cells[y+i][x].pieceInCell != None):
                if(cells[y+i][x].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y+i][x].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y+i][x])
                    collided = True
            elif(cells[y+i][x].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(cells[y+i][x])
    collided = False
    for i in range(1, 8):
           if((y-i) in range(8)):
            if(cells[y-i][x].pieceInCell != None):
                if(cells[y-i][x].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y-i][x].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y-i][x])
                    collided = True
            elif(cells[y-i][x].pieceInCell == None and not collided):
                selectedPiece.possibleMoves.append(cells[y-i][x])

def CheckPrimalDiagonal(cells, x, y, selectedPiece):
    collided = False
    for i in range(1,8):
        if((y+i) in range(8) and (x+i) in range(8)):
            if(cells[y+i][x+i].pieceInCell != None):
                if(cells[y+i][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y+i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y+i][x+i])
                    collided = True
            elif(cells[y+i][x+i].pieceInCell == None and (not collided)):
                    selectedPiece.possibleMoves.append(cells[y+i][x+i])
    collided = False
    for i in range(1,8):
        if((y-i) in range(8) and (x-i) in range(8)):
            if(cells[y-i][x-i].pieceInCell != None):
                if(cells[y-i][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y-i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y-i][x-i])
                    collided = True
            elif(cells[y-i][x-i].pieceInCell == None and (not collided)):
                    selectedPiece.possibleMoves.append(cells[y-i][x-i])

def CheckSecondaryDiagonal(cells, x, y, selectedPiece):
    collided = False
    for i in range(1, 8):
        if((y+i) in range(8) and (x-i) in range(8)):
            if(cells[y+i][x-i].pieceInCell != None):
                if(cells[y+i][x-i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y+i][x-i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y+i][x-i])
                    collided = True
            elif(cells[y+i][x-i].pieceInCell == None and not collided):
                    selectedPiece.possibleMoves.append(cells[y+i][x-i])
    collided = False
    for i in range(1, 8):
        if((y-i) in range(8) and (x+i) in range(8)):
            if(cells[y-i][x+i].pieceInCell != None):
                if(cells[y-i][x+i].pieceInCell.color == selectedPiece.color):
                    break
                if(cells[y-i][x+i].pieceInCell.color != selectedPiece.color and collided == False):
                    selectedPiece.possibleMoves.append(cells[y-i][x+i])
                    collided = True
            elif(cells[y-i][x+i].pieceInCell == None and not collided):
                    selectedPiece.possibleMoves.append(cells[y-i][x+i])

def CheckDiagonally(cells, x, y, selectedPiece):
    CheckSecondaryDiagonal(cells, x, y, selectedPiece)
    CheckPrimalDiagonal(cells, x, y, selectedPiece)

def move_pawn(cells, x, y, selectedPiece):
    if(cells[y][x].pieceInCell.color == Enums.Color.BLACK):
        if(y == 1 and cells[y+2][x].pieceInCell == None and cells[y+1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+2][x])
        if((y+1)in range(8) and (x-1) in range(8) and cells[y+1][x-1].pieceInCell != None and cells[y+1][x-1].pieceInCell.color == Enums.Color.WHITE):
            selectedPiece.possibleMoves.append(cells[y+1][x-1])
        if((y+1)in range(8) and (x+1) in range(8) and cells[y+1][x+1].pieceInCell != None and cells[y+1][x+1].pieceInCell.color == Enums.Color.WHITE):
            selectedPiece.possibleMoves.append(cells[y+1][x+1])
        if((y+1) in range (8) and cells[y+1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+1][x])

    else:
        if(y == 6 and cells[y-2][x].pieceInCell == None and cells[y-1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-2][x])
        if((y-1)in range(8) and (x-1) in range(8) and cells[y-1][x-1].pieceInCell != None and cells[y-1][x-1].pieceInCell.color == Enums.Color.BLACK):
            selectedPiece.possibleMoves.append(cells[y-1][x-1])
        if((y-1)in range(8) and (x+1) in range(8) and cells[y-1][x+1].pieceInCell != None and cells[y-1][x+1].pieceInCell.color == Enums.Color.BLACK):
            selectedPiece.possibleMoves.append(cells[y-1][x+1])
        if((y-1) in range (8) and cells[y-1][x].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-1][x])

def move_bishop(cells, x, y, selectedPiece):
    CheckDiagonally(cells, x, y, selectedPiece)

def move_king(cells, x, y, selectedPiece):
    if((y-1)in range(8) and (x+1) in range(8) and cells[y-1][x+1].pieceInCell != None and cells[y-1][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y-1][x+1])
    if((y+1)in range(8) and (x+1) in range(8) and cells[y+1][x+1].pieceInCell != None and cells[y+1][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y+1][x+1])
    if((y+1)in range(8) and (x-1) in range(8) and cells[y+1][x-1].pieceInCell != None and cells[y+1][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y+1][x-1])
    if((y-1)in range(8) and (x-1) in range(8) and cells[y-1][x-1].pieceInCell != None and cells[y-1][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y-1][x-1])

    if((y-1)in range(8) and cells[y-1][x].pieceInCell != None and cells[y-1][x].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y-1][x])
    if((y+1)in range(8) and cells[y+1][x].pieceInCell != None and cells[y+1][x].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y+1][x])
    if((x-1) in range(8) and cells[y][x-1].pieceInCell != None and cells[y][x-1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y][x-1])
    if((x+1) in range(8) and cells[y][x+1].pieceInCell != None and cells[y][x+1].pieceInCell.color != selectedPiece.color):
        selectedPiece.possibleMoves.append(cells[y][x+1])

    if((y+1) in range (8) and cells[y+1][x].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y+1][x])
    if((y-1) in range (8) and cells[y-1][x].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y-1][x])
    if((x+1) in range (8) and cells[y][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y][x+1])
    if((x-1) in range (8) and cells[y][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y][x-1])

    if((y+1) in range (8) and (x+1) in range(8) and cells[y+1][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y+1][x+1])
    if((y-1) in range (8) and (x-1) in range(8) and cells[y-1][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y-1][x-1])
    if((y-1) in range(8) and (x+1) in range (8) and cells[y-1][x+1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y-1][x+1])
    if((y+1) in range(8) and (x-1) in range (8) and cells[y+1][x-1].pieceInCell == None):
        selectedPiece.possibleMoves.append(cells[y+1][x-1])

def move_queen(cells, x, y, selectedPiece):
    CheckHorizontal(cells, x, y, selectedPiece)
    CheckDiagonally(cells, x, y, selectedPiece)
    CheckVertical(cells, x, y, selectedPiece)

def move_rook(cells, x, y, selectedPiece):
    CheckHorizontal(cells, x, y, selectedPiece)
    CheckVertical(cells, x, y, selectedPiece)

def move_knight(cells, x, y, selectedPiece):
    if((y-2) in range(8) and (x+1) in range(8)):
        if(cells[y-2][x+1].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-2][x+1])
        else:
            if(cells[y-2][x+1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y-2][x+1])

    if((y-2) in range(8) and (x-1) in range(8)):
        if(cells[y-2][x-1].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-2][x-1])
        else:
            if(cells[y-2][x-1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y-2][x-1])

    if((y+2) in range(8) and (x+1) in range(8)):
        if(cells[y+2][x+1].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+2][x+1])
        else:
            if(cells[y+2][x+1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y+2][x+1])

    if((y+2) in range(8) and (x-1) in range(8)):
        if(cells[y+2][x-1].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+2][x-1])
        else:
            if(cells[y+2][x-1].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y+2][x-1])

    
    if((y+1) in range(8) and (x-2) in range(8)):
        if(cells[y+1][x-2].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+1][x-2])
        else:
            if(cells[y+1][x-2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y+1][x-2])
    
    if((y-1) in range(8) and (x+2) in range(8)):
        if(cells[y-1][x+2].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-1][x+2])
        else:
            if(cells[y-1][x+2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y-1][x+2])
    
    if((y-1) in range(8) and (x-2) in range(8)):
        if(cells[y-1][x-2].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y-1][x-2])
        else:
            if(cells[y-1][x-2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y-1][x-2])

    
    if((y+1) in range(8) and (x+2) in range(8)):
        if(cells[y+1][x+2].pieceInCell == None):
            selectedPiece.possibleMoves.append(cells[y+1][x+2])
        else:
            if(cells[y+1][x+2].pieceInCell.color != selectedPiece.color):
                selectedPiece.possibleMoves.append(cells[y+1][x+2])
                    
moves = {
    Enums.PieceType.PAWN : move_pawn,
    Enums.PieceType.BISHOP : move_bishop,
    Enums.PieceType.KING : move_king,
    Enums.PieceType.QUEEN : move_queen,
    Enums.PieceType.KNIGHT : move_knight,
    Enums.PieceType.ROOK : move_rook
}