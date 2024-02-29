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

def CheckForCheckMate(piece, x, y):
    if piece.type != Enums.PieceType.KING:
        pass
