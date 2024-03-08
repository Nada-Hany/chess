from turtle import right
import Piece, Enums, Board
import pygame, os
# not checkmate

def CheckForGameOver(deadPiece):
    # return false if black wins, true if white wins
    if deadPiece.type == Enums.PieceType.KING:
        if deadPiece.color == Enums.Color.WHITE:
            return False
        else:
            return True
    return None

def DrawGameOver(window, width, height, text):
    color = (90,50,30)
    font = pygame.font.SysFont('comicsans', 120)
    obj = font.render(text, True, color)
    window.blit(obj, (width//2 - (obj.get_width()//2) , height//2 - (obj.get_height()//2))) 

def DrawPlayerTurn(window, width, whiteTurn):
    font = pygame.font.SysFont('comicsans', 32)
    playerText = ""
    color = (255, 255, 255)
    if(whiteTurn == True):
        playerText = "white turn"
    else:
        playerText = "black turn"
    obj = font.render(playerText, True, color)
    window.blit(obj, (width//2 - (obj.get_width()//2) , 0))

def CheckForCastleMoves(piece, x, y, cells):
    empty = True
    rightCol = 7; leftCol = 0; middleCol = 4
    if(piece.type == Enums.PieceType.KING and piece.moved == False):
        # (king)...right rook
        for i in range(x+1, 7):
            if(cells[y][i].pieceInCell != None):
                empty = False
        KingCastle(empty, piece, rightCol, y, cells)
        empty = True
        # left rook....(king)
        for i in range(1, x):
            if(cells[y][i].pieceInCell != None):
                empty = False
        KingCastle(empty, piece, leftCol, y, cells)
    elif(piece.type == Enums.PieceType.ROOK and piece.moved == False):
        empty = True
        # (left rook)......king
        if x == 0:
            for i in range(1, middleCol):
                if(cells[y][i].pieceInCell != None):
                    empty = False
            RookCastle(empty, piece, middleCol, y, cells)
        # king ......(right rook)
        else:
            empty = True
            for i in range(middleCol+1, 7):
                if(cells[y][i].pieceInCell != None):
                    empty = False
            RookCastle(empty, piece, middleCol, y, cells)

def RookCastle(empty, piece:Piece.piece, middleCol, y, cells):
    if empty:
        if(cells[y][middleCol].pieceInCell != None and cells[y][middleCol].pieceInCell.type == Enums.PieceType.KING
            and cells[y][middleCol].pieceInCell.moved == False):
            Board.board.possibleMoves.append(cells[y][middleCol])
            piece.canCastle = True

def KingCastle(empty, piece: Piece.piece, col, y, cells):
    if empty:
            if(cells[y][col].pieceInCell != None and cells[y][col].pieceInCell.type == Enums.PieceType.ROOK and 
                cells[y][col].pieceInCell.moved == False):
                Board.board.possibleMoves.append(cells[y][col])
                piece.canCastle = True

def CheckForPawnPromoption(piece:Piece.piece, y, boardObj):   
    if(piece.type == Enums.PieceType.PAWN and 
       piece.color == Enums.Color.BLACK):
        if(y == 7):
            boardObj.pawnPromotion = True

    elif(piece.type == Enums.PieceType.PAWN and 
            piece.color == Enums.Color.WHITE):
        if y == 0:
            boardObj.pawnPromotion = True 

def SetPossiblePromotions(color):
    queen_image =""; rook_image = ""; bishop_image = ""; knight_image = ""
    if color == Enums.Color.BLACK:
        queen_image = pygame.image.load(os.path.join('assets','black-queen.png'))
        knight_image = pygame.image.load(os.path.join('assets','black-knight.png'))
        rook_image = pygame.image.load(os.path.join('assets','black-rook.png')) 
        bishop_image = pygame.image.load(os.path.join('assets','black-bishop.png'))
    else:
        queen_image = pygame.image.load(os.path.join('assets','white-queen.png'))
        knight_image = pygame.image.load(os.path.join('assets','white-knight.png'))
        rook_image = pygame.image.load(os.path.join('assets','white-rook.png')) 
        bishop_image = pygame.image.load(os.path.join('assets','white-bishop.png'))

    queen_image = pygame.transform.scale(queen_image, (80, 80))
    rook_image = pygame.transform.scale(rook_image, (80, 80))
    bishop_image = pygame.transform.scale(bishop_image, (80, 80))
    knight_image = pygame.transform.scale(knight_image, (80, 80))

    possiblePromotion = []
    possiblePromotion.append(rook_image)
    possiblePromotion.append(queen_image)
    possiblePromotion.append(bishop_image)
    possiblePromotion.append(knight_image)
    # rook , queen , bishop , knight
    return possiblePromotion

def DrawPossiblePromotion(window, color, width, height):
    possiblePromotions = SetPossiblePromotions(color)
    # x y width height
    x = width//2 - 320//2
    y = height//2-80//2
    pygame.draw.rect(window, (90,50,30), (x, y, 320, 80))
    i = 0
    # rook , queen , bishop , knight
    for piece in possiblePromotions:
      window.blit(piece, (i*80 + x, y))
      i+=1

def HandlPromotionSelection(position, xOffset, yOffset, tileSize, boardObj):
     # rook , queen , bishop , knight
    x = (position[0] - xOffset) // tileSize
    y = position[1] 
    valid = False
    if y in range(yOffset, yOffset+80):
        if x == 0:
            boardObj.pawnToBePromoted.SetRook(boardObj.pawnToBePromoted.color)
            valid = True
        elif x == 1:
            boardObj.pawnToBePromoted.SetQueen(boardObj.pawnToBePromoted.color)
            valid = True
        elif x == 2:
            boardObj.pawnToBePromoted.SetBishop(boardObj.pawnToBePromoted.color)
            valid = True
        elif x == 3:
            boardObj.pawnToBePromoted.SetKnight(boardObj.pawnToBePromoted.color)
            valid = True
    if valid:
        if(boardObj.pawnToBePromoted.color == Enums.Color.BLACK):
            boardObj.cells[7][boardObj.pawnToBePromoted.previousY].pieceInCell = boardObj.pawnToBePromoted

        else:
            boardObj.cells[0][boardObj.pawnToBePromoted.previousY].pieceInCell = boardObj.pawnToBePromoted
        boardObj.cells[boardObj.pawnToBePromoted.previousX][boardObj.pawnToBePromoted.previousY].pieceInCell = None
        boardObj.pawnPromotion = False

'''we can make two type of checkmate checking:
    first -> checking for the king move itself that its valid and won't put him in check
    second -> checking for any ally piece moving and checking wheather this move will put the king in check or not 
    for any of the moves it won't be a valid move anymore'''

# if the king moved horizontally we check vertically/diagonally
# if moved vaertically we check horizontally/diagonally
# if moved diagonally we check vertivally/horizontally

#pawn always diagonally---
def HorizontalliInvalids(piece, x, y, board):
    # right -> same y -- x+1
    for i in range(x,8):
        if(board.cells[y][i].pieceInCell != None):
            if(board.cells[y][i].pieceInCell.color == piece.color):
                break
            else:
                if(board.cells[y][i].pieceInCell.type == Enums.PieceType.QUEEN or
                board.cells[y][i].pieceInCell.type == Enums.PieceType.ROOK):
                    piece.invalidMoves.append((y,x))
                    break
                if(board.cells[y][i].pieceInCell.type == Enums.PieceType.KING 
                and (x+1) in range(8) and i == x+1):
                    piece.invalidMoves.append((y,x))
                    break
    # left -> same y , x-1
    for i in range(x,0,-1):
        if(board.cells[y][i].pieceInCell != None):
            if(board.cells[y][i].pieceInCell.color == piece.color):
                break
            else:
                if(board.cells[y][i].pieceInCell.type == Enums.PieceType.QUEEN or
                board.cells[y][i].pieceInCell.type == Enums.PieceType.ROOK):
                    piece.invalidMoves.append((y,x))
                    break
                if(board.cells[y][i].pieceInCell.type == Enums.PieceType.KING 
                and (x-1)in range(8) and i == x-1):
                    piece.invalidMoves.append((y,x))
                    break
    
def VerticallyInvalids(piece, x, y, board):
    # downward -> same x and y-1
    for i in range(y,8):
        if(board.cells[i][x].pieceInCell != None):
            if(board.cells[i][x].pieceInCell.color == piece.color):
                break
            else:
                if not (board.cells[i][x].pieceInCell.type == Enums.PieceType.QUEEN or
                    board.cells[i][x].pieceInCell.type == Enums.PieceType.ROOK or
                    board.cells[i][x].pieceInCell.type == Enums.PieceType.KING):
                    break   
                if(board.cells[i][x].pieceInCell.type == Enums.PieceType.QUEEN or
                board.cells[i][x].pieceInCell.type == Enums.PieceType.ROOK):
                    piece.invalidMoves.append((y,x))
                    break
                if(board.cells[i][x].pieceInCell.type == Enums.PieceType.KING 
                and y-1 in range(8) and i == y-1):
                    piece.invalidMoves.append((y,x))
                    break
    # upwards -> same x and y+1
    for i in range(y,0, -1):
        if(board.cells[i][x].pieceInCell != None):
            if(board.cells[i][x].pieceInCell.color == piece.color):
                break
            else:
                if (board.cells[i][x].pieceInCell.type != Enums.PieceType.QUEEN and
                    board.cells[i][x].pieceInCell.type != Enums.PieceType.ROOK and
                    board.cells[i][x].pieceInCell.type != Enums.PieceType.KING):
                    break
                if(board.cells[i][x].pieceInCell.type == Enums.PieceType.QUEEN or
                    board.cells[i][x].pieceInCell.type == Enums.PieceType.ROOK):
                        piece.invalidMoves.append((y,x))
                        break
                if(board.cells[i][x].pieceInCell.type == Enums.PieceType.KING 
                and (y+1) in range(8) and i == y+1):
                    piece.invalidMoves.append((y,x))
                    break
                else:
                    break

def DiagonallyInvalids(piece, x, y, board):
    # bottom right
    for i in range(1,8):
        if((y+i) in range(8) and (x+i) in range(8)):
            if(board.cells[y+i][x+i].pieceInCell != None):
                if(board.cells[y+i][x+i].pieceInCell.color == piece.color):
                    break
                else:
                    if(board.cells[y+i][x+i].pieceInCell.type == Enums.PieceType.BISHOP or
                       board.cells[y+i][x+i].pieceInCell.type == Enums.PieceType.QUEEN):
                        piece.invalidMoves.append((y,x))
                        break
                    if((board.cells[y+i][x+i].pieceInCell.type == Enums.PieceType.KING or
                        board.cells[y+i][x+i].pieceInCell.type == Enums.PieceType.PAWN) and
                        y+i == y+1 and x+i == x+1):
                        piece.invalidMoves.append((y,x))
                        break
    # bottom left
    for i in range(1,8):
        if((y+i) in range(8) and (x-i) in range(8)):
            if(board.cells[y+i][x-i].pieceInCell != None):
                if(board.cells[y+i][x-i].pieceInCell.color == piece.color):
                    break
                else:   
                    if(board.cells[y+i][x-i].pieceInCell.type == Enums.PieceType.BISHOP or
                       board.cells[y+i][x-i].pieceInCell.type == Enums.PieceType.QUEEN):
                        piece.invalidMoves.append((y,x))
                        break
                    if((board.cells[y+i][x-i].pieceInCell.type == Enums.PieceType.KING or
                        board.cells[y+i][x-i].pieceInCell.type == Enums.PieceType.PAWN) and
                        y+i == y+1 and x-i == x-1):
                        piece.invalidMoves.append((y,x))
                        break            
    # top left
    for i in range(1,8):
        if((y-i) in range(8) and (x-i) in range(8)):
            if(board.cells[y-i][x-i].pieceInCell != None):
                if(board.cells[y-i][x-i].pieceInCell.color == piece.color):
                    break
                else:
                    if(board.cells[y-i][x-i].pieceInCell.type == Enums.PieceType.BISHOP or
                       board.cells[y-i][x-i].pieceInCell.type == Enums.PieceType.QUEEN):
                        piece.invalidMoves.append((y,x))
                        break
                    if((board.cells[y-i][x-i].pieceInCell.type == Enums.PieceType.KING or
                        board.cells[y-i][x-i].pieceInCell.type == Enums.PieceType.PAWN) and
                        y-i == y-1 and x-i == x-1):
                        piece.invalidMoves.append((y,x))
                        break
    # top right
    for i in range(1,8):
        if((y-i) in range(8) and (x+i) in range(8)):
            if(board.cells[y-i][x+i].pieceInCell != None):
                if(board.cells[y-i][x+i].pieceInCell.color == piece.color):
                    break
                else:
                    if(board.cells[y-i][x+i].pieceInCell.type == Enums.PieceType.BISHOP or
                       board.cells[y-i][x+i].pieceInCell.type == Enums.PieceType.QUEEN):
                        piece.invalidMoves.append((y,x))
                        break
                    if((board.cells[y-i][x+i].pieceInCell.type == Enums.PieceType.KING or
                        board.cells[y-i][x+i].pieceInCell.type == Enums.PieceType.PAWN) and
                        y-i == y-1 and x+i == x+1):
                        piece.invalidMoves.append((y,x))
                        break

def KnightInvalids(piece, x, y, board):
    if((y-2) in range(8) and (x+1) in range(8)):
        if(board.cells[y-2][x+1].pieceInCell != None and board.cells[y-2][x+1].pieceInCell.color != piece.color):
            piece.invalidMoves.append((y,x))
            

    if((y-2) in range(8) and (x-1) in range(8)):
        if(board.cells[y-2][x-1].pieceInCell != None and board.cells[y-2][x-1].pieceInCell.color != piece.color):
            piece.invalidMoves.append((y,x))
                

    if((y+2) in range(8) and (x+1) in range(8)):
        if(board.cells[y+2][x+1].pieceInCell == None):
            piece.invalidMoves.append((y,x))   
        else:
            if(board.cells[y+2][x+1].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))

    if((y+2) in range(8) and (x-1) in range(8)):
        if(board.cells[y+2][x-1].pieceInCell != None and board.cells[y+2][x-1].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))

    
    if((y+1) in range(8) and (x-2) in range(8)):
        if(board.cells[y+1][x-2].pieceInCell != None and board.cells[y+1][x-2].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))
    
    if((y-1) in range(8) and (x+2) in range(8)):
        if(board.cells[y-1][x+2].pieceInCell != None and board.ells[y-1][x+2].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))
    
    if((y-1) in range(8) and (x-2) in range(8)):
        if(board.cells[y-1][x-2].pieceInCell != None and board.cells[y-1][x-2].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))

    if((y+1) in range(8) and (x+2) in range(8)):
        if(board.cells[y+1][x+2].pieceInCell != None and board.cells[y+1][x+2].pieceInCell.color != piece.color):
                piece.invalidMoves.append((y,x))

def GetCheckMates(piece, x, y, board):
    # above
    piece.invalidMoves.clear()
    if((y-1) in range(8) and board.cells[y-1][x].pieceInCell == None):
        HorizontalliInvalids(piece, x, y-1, board)
        DiagonallyInvalids(piece, x, y-1, board)
        print(piece.invalidMoves)

    # down
    if((y+1) in range(8) and board.cells[y+1][x].pieceInCell == None):
        HorizontalliInvalids(piece, x, y+1, board)
        DiagonallyInvalids(piece, x, y+1, board)
    # right
    if((x+1) in range(8) and board.cells[y][x+1].pieceInCell == None):
        VerticallyInvalids(piece, x+1, y, board)
        DiagonallyInvalids(piece, x+1, y, board)
    # left
    if((x-1) in range(8) and board.cells[y][x-1].pieceInCell == None):
        VerticallyInvalids(piece, x-1, y, board)
        DiagonallyInvalids(piece, x-1, y, board)
    # right top
    if((y-1) in range(8) and (x+1) in range(8) and board.cells[y-1][x+1].pieceInCell == None):
        DiagonallyInvalids(piece, x+1, y-1, board)
        VerticallyInvalids(piece, x+1, y-1, board)
        HorizontalliInvalids(piece, x+1, y-1, board)

    # left top
    if((y-1) in range(8) and (x-1) in range(8) and board.cells[y-1][x-1].pieceInCell == None):
        VerticallyInvalids(piece, x-1, y-1, board)
        DiagonallyInvalids(piece, x-1, y-1, board)
        HorizontalliInvalids(piece, x-1, y-1, board)

    # right bottom
    if((y+1) in range(8) and (x+1) in range(8) and board.cells[y+1][x+1].pieceInCell == None):
        VerticallyInvalids(piece, x+1, y+1, board)
        DiagonallyInvalids(piece, x+1, y+1, board)
        HorizontalliInvalids(piece, x+1, y+1, board)
    # left bottom
    if((y+1) in range(8) and (x-1) in range(8) and board.cells[y+1][x-1].pieceInCell == None):
        VerticallyInvalids(piece, x-1, y+1, board)
        DiagonallyInvalids(piece, x-1, y+1, board)
        HorizontalliInvalids(piece, x-1, y+1, board)

