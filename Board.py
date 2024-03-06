import Enums, Piece, Cell
from move_logic import *
from game_events import *
import pygame
import os

class board:
    
    selectedPiece = None 
    pawnInPromotion = None
    possibleMoves = []
    blackDeadPieces = []
    whiteDeadPieces = []
    whiteTurn = True
    whitePlayerMoved = False
    gameOver = None
    pawnToBePromoted = None
    
    def __init__(self, tilesNumber,color1, color2, tileSize, xOffset, yOffset, window, width, height):
        self.tilesNumber = tilesNumber
        self.window = window
        self.color1 = color1
        self.color2 = color2
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.tileSize = tileSize
        self.width = width
        self.height = height
        self.pawnPromotion = False
        self.cells = [[Cell.cell(xOffset + x*tileSize,yOffset + y*tileSize) for x in range(8)] for y in range(8)]
    
    def DrawBoard(self, window):
        for i in range(self.tilesNumber):
            for g in range(self.tilesNumber):
                if((i + g) % 2 == 0):
                     pygame.draw.rect(window, self.color1, (g*self.tileSize +self.xOffset, i*self.tileSize+self.yOffset,self.tileSize, self.tileSize))
                else:
                    pygame.draw.rect(window, self.color2, (g*self.tileSize +self.xOffset, i*self.tileSize+self.yOffset,self.tileSize, self.tileSize))
        for deadPiece in self.blackDeadPieces:
            deadPiece.image = pygame.transform.scale(deadPiece.image, (40, 40))
            index = self.blackDeadPieces.index(deadPiece)
            if(index > 12):
                window.blit(deadPiece.image, (self.xOffset - 120, self.yOffset + (index - 13) * 50))
            else:
                window.blit(deadPiece.image, (self.xOffset - 60, self.yOffset + index * 50 ))
        for deadPiece in self.whiteDeadPieces:
            deadPiece.image = pygame.transform.scale(deadPiece.image, (40, 40))
            index = self.whiteDeadPieces.index(deadPiece)
            if(index > 12):
                window.blit(deadPiece.image, (self.xOffset + self.tilesNumber*self.tileSize + 120,self.yOffset + (index - 13) * 50 ))
            else:
                window.blit(deadPiece.image, (self.xOffset + self.tilesNumber*self.tileSize + 20,self.yOffset + index * 50 ))

    def InitializePieces(self):
        BLACK, WHITE = Enums.Color.BLACK, Enums.Color.WHITE
        PAWN = Enums.PieceType.PAWN
        BISHOP = Enums.PieceType.BISHOP
        KING = Enums.PieceType.KING
        QUEEN = Enums.PieceType.QUEEN
        ROOK = Enums.PieceType.ROOK
        KNIGHT = Enums.PieceType.KNIGHT

        black_bishp_img = pygame.image.load(os.path.join('assets','black-bishop.png'))
        black_king_img = pygame.image.load(os.path.join('assets','black-king.png'))
        black_knight_img = pygame.image.load(os.path.join('assets','black-knight.png'))
        black_pawn_img = pygame.image.load(os.path.join('assets','black-pawn.png'))
        black_queen_img = pygame.image.load(os.path.join('assets','black-queen.png'))
        black_rook_img = pygame.image.load(os.path.join('assets','black-rook.png'))

        white_pawn_img = pygame.image.load(os.path.join('assets','white-pawn.png'))
        white_bishp_img = pygame.image.load(os.path.join('assets','white-bishop.png'))
        white_king_img = pygame.image.load(os.path.join('assets','white-king.png'))
        white_knight_img = pygame.image.load(os.path.join('assets','white-knight.png'))
        white_queen_img = pygame.image.load(os.path.join('assets','white-queen.png'))
        white_rook_img = pygame.image.load(os.path.join('assets','white-rook.png'))

        black_rook_left = Piece.piece(BLACK, ROOK, True, False, black_rook_img)
        self.cells[0][0].SetPiece(black_rook_left)
        black_rook_right = Piece.piece(BLACK, ROOK, True, False, black_rook_img)
        self.cells[0][7].SetPiece(black_rook_right)
        black_knight_left = Piece.piece(BLACK, KNIGHT, True, False, black_knight_img)
        self.cells[0][1].SetPiece(black_knight_left)
        black_rook_left.SetInitialCor(0, 0)
        black_knight_right = Piece.piece(BLACK, KNIGHT, True, False, black_knight_img)
        self.cells[0][6].SetPiece(black_knight_right)
        black_rook_right.SetInitialCor(0, 7)
        black_bishop_left = Piece.piece(BLACK, BISHOP, True, False, black_bishp_img)
        self.cells[0][2].SetPiece(black_bishop_left)
        black_bishop_right = Piece.piece(BLACK, BISHOP, True, False, black_bishp_img)
        self.cells[0][5].SetPiece(black_bishop_right)
        black_queen = Piece.piece(BLACK, QUEEN, True, False, black_queen_img)
        self.cells[0][3].SetPiece(black_queen)
        black_king = Piece.piece(BLACK, KING, True, False, black_king_img)
        self.cells[0][4].SetPiece(black_king)
        black_king.SetInitialCor(0, 4)
        black_pawn1 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][0].SetPiece(black_pawn1)
        black_pawn2 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][1].SetPiece(black_pawn2)
        black_pawn3 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][2].SetPiece(black_pawn3)
        black_pawn4 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][3].SetPiece(black_pawn4)
        black_pawn5 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][4].SetPiece(black_pawn5)
        black_pawn6 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][5].SetPiece(black_pawn6)
        black_pawn7 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][6].SetPiece(black_pawn7)
        black_pawn8 =Piece.piece(BLACK, PAWN, True, False, black_pawn_img)
        self.cells[1][7].SetPiece(black_pawn8)

        white_rook_left = Piece.piece(WHITE, ROOK, True, False, white_rook_img)
        self.cells[7][0].SetPiece(white_rook_left)
        white_rook_left.SetInitialCor(7, 0)
        white_rook_right = Piece.piece(WHITE, ROOK, True, False, white_rook_img)
        self.cells[7][7].SetPiece(white_rook_right)
        white_rook_right.SetInitialCor(7, 7)
        white_knight_left = Piece.piece(WHITE, KNIGHT, True, False, white_knight_img)
        self.cells[7][1].SetPiece(white_knight_left)
        white_knight_right = Piece.piece(WHITE, KNIGHT, True, False, white_knight_img)
        self.cells[7][6].SetPiece(white_knight_right)
        white_bishop_left = Piece.piece(WHITE, BISHOP, True, False, white_bishp_img)
        self.cells[7][2].SetPiece(white_bishop_left)
        white_bishop_right = Piece.piece(WHITE, BISHOP, True, False, white_bishp_img)
        self.cells[7][5].SetPiece(white_bishop_right)
        white_queen = Piece.piece(WHITE, QUEEN, True, False, white_queen_img)
        self.cells[7][3].SetPiece(white_queen)
        white_king = Piece.piece(WHITE, KING, True, False, white_king_img)
        self.cells[7][4].SetPiece(white_king)
        white_king.SetInitialCor(7, 4)
        white_pawn1 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][0].SetPiece(white_pawn1)
        white_pawn2 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][1].SetPiece(white_pawn2)
        white_pawn3 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][2].SetPiece(white_pawn3)
        white_pawn4 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][3].SetPiece(white_pawn4)
        white_pawn5 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][4].SetPiece(white_pawn5)
        white_pawn6 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][5].SetPiece(white_pawn6)
        white_pawn7 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][6].SetPiece(white_pawn7)
        white_pawn8 =Piece.piece(WHITE, PAWN, True, False, white_pawn_img)
        self.cells[6][7].SetPiece(white_pawn8)
    
    def setSelectedPiece(self, x, y, piece):
        self.cells[y][x].pieceInCell.previousX = y
        self.cells[y][x].pieceInCell.previousY = x
        self.selectedPiece = piece
        self.selectedPiece.possibleMoves.clear()
        moves[piece.type](x, y, self.selectedPiece, self)
        CheckForCastleMoves(self.selectedPiece, x, y, self.cells)
        if(piece.type == Enums.PieceType.KING):
            GetCheckMates(piece, x, y, self)
            print(piece.possibleMoves)
            print(piece.invalidMoves)
            
    def DrawPieces(self,window, pngOffsets):
        for cell in self.cells:
            for eachCell in cell:
                if(eachCell.pieceInCell != None):
                  eachCell.DrawPiece(window, pngOffsets)
        if(self.selectedPiece != None):
            for cell in self.selectedPiece.possibleMoves:
                if cell not in self.selectedPiece.invalidMoves:
                    self.DrawMove(window, cell.x, cell.y)

    def DrawMove(self, window, x, y):
        pygame.draw.rect(window, (200, 0, 0), (x + 2, y + 2, 76, 76), 4)

    def HandlMovement(self, position):
        # x -> col, y-> row
        x = (position[0] - self.xOffset) // self.tileSize
        y = (position[1] - self.yOffset) // self.tileSize
        if(y in range(8) and x in range(8)):
            inCell = self.cells[y][x].pieceInCell
            # if chosen cell is not empty
            if(inCell != None):
                if(self.selectedPiece != None):
                    # changing the selected piece 
                    if(self.cells[y][x].pieceInCell.color == self.selectedPiece.color and 
                       not self.selectedPiece.canCastle):
                        self.setSelectedPiece(x, y, self.cells[y][x].pieceInCell)
                    # moving the selected piece to a valid position
                    for cell in self.selectedPiece.possibleMoves:
                        if (y == ((cell.y - self.yOffset)//self.tileSize)) and (x == ((cell.x - self.xOffset)//self.tileSize)):
                            # kill enemy
                            if(self.cells[y][x].pieceInCell.color != self.selectedPiece.color):
                                if(self.selectedPiece.color == Enums.Color.WHITE):
                                    self.blackDeadPieces.append(self.cells[y][x].pieceInCell)
                                else:
                                    self.whiteDeadPieces.append(self.cells[y][x].pieceInCell)
                                self.gameOver = CheckForGameOver(self.cells[y][x].pieceInCell)
                                self.MovePiece(y, x)
                            # casteling
                            else:
                                if(self.selectedPiece.canCastle):
                                    self.CastleMove(y, x)
                # selecting a piece 
                else:
                    if((self.whiteTurn and inCell.color == Enums.Color.WHITE) or (not self.whiteTurn and inCell.color == Enums.Color.BLACK)):
                        self.setSelectedPiece(x, y, inCell)
            else:
                # a piece is selected and its time to move it
                if(self.selectedPiece != None):
                    for cell in self.selectedPiece.possibleMoves:
                            if (y == ((cell.y - self.yOffset)//self.tileSize)) and (x == ((cell.x - self.xOffset)//self.tileSize)):
                                # move
                                if cell not in self.selectedPiece.invalidMoves:
                                    if(self.cells[y][x].pieceInCell == None):
                                        self.MovePiece(y, x)
   
    def MovePiece(self, y, x):
        self.cells[y][x].pieceInCell = self.selectedPiece
        CheckForPawnPromoption(self.selectedPiece, y, self)
        if self.pawnPromotion:
            self.pawnToBePromoted = self.selectedPiece
        self.cells[self.selectedPiece.previousX][self.selectedPiece.previousY].pieceInCell = None
        CheckForPawnPromoption(self.selectedPiece, y, self)
        if(self.pawnPromotion):
            self.pawnInPromotion = self.selectedPiece
            self.pawnColor = self.selectedPiece.color
        self.Move()
        
    def Move(self):
        if(self.whiteTurn):
            self.whiteTurn = False
        else:
            self.whiteTurn = True
        self.selectedPiece.Moved()
        self.selectedPiece = None

    def CastleMove(self, y, x):

        if self.selectedPiece.type == Enums.PieceType.KING:
            # king casteling to the right
            if x > self.selectedPiece.previousY:
                self.cells[y][7].pieceInCell.Moved()
                self.cells[y][7].pieceInCell.canCastle = False
                self.cells[y][self.selectedPiece.kingCastleRightX].pieceInCell = self.selectedPiece
                self.cells[y][self.selectedPiece.rightRookCastleX].pieceInCell = self.cells[y][7].pieceInCell
                self.cells[y][7].pieceInCell = None
            # king casteling to the left
            else:
                self.cells[y][0].pieceInCell.Moved()
                self.cells[y][0].pieceInCell.canCastle = False
                self.cells[y][self.selectedPiece.kingCastleLeftX].pieceInCell = self.selectedPiece
                self.cells[y][self.selectedPiece.leftRookCastleX].pieceInCell = self.cells[y][0].pieceInCell
                self.cells[y][0].pieceInCell = None

        elif self.selectedPiece.type == Enums.PieceType.ROOK:
            self.cells[y][4].pieceInCell.Moved()
            self.cells[y][4].pieceInCell.canCastle = False
            # left rook casteling
            if x > self.selectedPiece.previousY:
                self.cells[y][self.selectedPiece.leftRookCastleX].pieceInCell = self.selectedPiece
                self.cells[y][self.selectedPiece.kingCastleLeftX].pieceInCell = self.cells[y][4].pieceInCell
                self.cells[y][4].pieceInCell = None
            # right rook casteling
            else:
                self.cells[y][self.selectedPiece.rightRookCastleX].pieceInCell = self.selectedPiece
                self.cells[y][self.selectedPiece.kingCastleRightX].pieceInCell = self.cells[y][4].pieceInCell
                self.cells[y][4].pieceInCell = None
        self.cells[self.selectedPiece.previousX][self.selectedPiece.previousY].pieceInCell = None
        self.selectedPiece.canCastle = False
        self.Move()