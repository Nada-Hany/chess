import Piece, Enums, Board
import pygame
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
    font = pygame.font.SysFont('comicsans', 130)
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
    piece.castleY = y
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
