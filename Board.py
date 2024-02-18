import Enums, Piece, Cell
import pygame
import os
class board:
 
    def __init__(self, tilesNumber,color1, color2, tileSize, xOffset, yOffset):
        self.tilesNumber = tilesNumber
        self.color1 = color1
        self.color2 = color2
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.tileSize = tileSize
        self.cells = [[Cell.cell(xOffset + x*tileSize,yOffset + y*tileSize) for x in range(8)] for y in range(8)]
    def DrawBoard(self, window):

        for i in range(self.tilesNumber):
            for g in range(self.tilesNumber):
                if((i + g) % 2 == 0):
                     pygame.draw.rect(window, self.color1, (g*self.tileSize +self.xOffset, i*self.tileSize+self.yOffset,self.tileSize, self.tileSize))
                else:
                    pygame.draw.rect(window, self.color2, (g*self.tileSize +self.xOffset, i*self.tileSize+self.yOffset,self.tileSize, self.tileSize))
        self.InitializePieces()

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
        
        black_rook_left = Piece.piece(BLACK, True, False, ROOK, black_rook_img)
        self.cells[0][0].setPiece(black_rook_left)
        black_rook_right = Piece.piece(BLACK, True, False, ROOK, black_rook_img)
        self.cells[0][7].setPiece(black_rook_right)
        black_knight_left = Piece.piece(BLACK, True, False, KNIGHT, black_knight_img)
        self.cells[0][1].setPiece(black_knight_left)
        black_knight_right = Piece.piece(BLACK, True, False, KNIGHT, black_knight_img)
        self.cells[0][6].setPiece(black_knight_right)
        black_bishop_left = Piece.piece(BLACK, True, False, BISHOP, black_bishp_img)
        self.cells[0][2].setPiece(black_bishop_left)
        black_bishop_right = Piece.piece(BLACK, True, False, BISHOP, black_bishp_img)
        self.cells[0][5].setPiece(black_bishop_right)
        black_queen = Piece.piece(BLACK, True, False, QUEEN, black_queen_img)
        self.cells[0][3].setPiece(black_queen)
        black_king = Piece.piece(BLACK, True, False, KING, black_king_img)
        self.cells[0][4].setPiece(black_king)
        black_pawn1 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][0].setPiece(black_pawn1)
        black_pawn2 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][1].setPiece(black_pawn2)
        black_pawn3 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][2].setPiece(black_pawn3)
        black_pawn4 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][3].setPiece(black_pawn4)
        black_pawn5 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][4].setPiece(black_pawn5)
        black_pawn6 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][5].setPiece(black_pawn6)
        black_pawn7 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][6].setPiece(black_pawn7)
        black_pawn8 =Piece.piece(BLACK, True, False, PAWN, black_pawn_img)
        self.cells[1][7].setPiece(black_pawn8)

        white_rook_left = Piece.piece(WHITE, True, False, ROOK, white_rook_img)
        self.cells[7][0].setPiece(white_rook_left)
        white_rook_right = Piece.piece(WHITE, True, False, ROOK, white_rook_img)
        self.cells[7][7].setPiece(white_rook_right)
        white_knight_left = Piece.piece(WHITE, True, False, KNIGHT, white_knight_img)
        self.cells[7][1].setPiece(white_knight_left)
        white_knight_right = Piece.piece(WHITE, True, False, KNIGHT, white_knight_img)
        self.cells[7][6].setPiece(white_knight_right)
        white_bishop_left = Piece.piece(WHITE, True, False, BISHOP, white_bishp_img)
        self.cells[7][2].setPiece(white_bishop_left)
        white_bishop_right = Piece.piece(WHITE, True, False, BISHOP, white_bishp_img)
        self.cells[7][5].setPiece(white_bishop_right)
        white_queen = Piece.piece(WHITE, True, False, QUEEN, white_queen_img)
        self.cells[7][3].setPiece(white_queen)
        white_king = Piece.piece(WHITE, True, False, KING, white_king_img)
        self.cells[7][4].setPiece(white_king)
        white_pawn1 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][0].setPiece(white_pawn1)
        white_pawn2 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][1].setPiece(white_pawn2)
        white_pawn3 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][2].setPiece(white_pawn3)
        white_pawn4 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][3].setPiece(white_pawn4)
        white_pawn5 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][4].setPiece(white_pawn5)
        white_pawn6 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][5].setPiece(white_pawn6)
        white_pawn7 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][6].setPiece(white_pawn7)
        white_pawn8 =Piece.piece(WHITE, True, False, PAWN, white_pawn_img)
        self.cells[6][7].setPiece(white_pawn8)

    def drawPieces(self,window, pngOffsets):
        for cell in self.cells:
            for eachCell in cell:
                if(eachCell.pieceInCell != None):
                  eachCell.drawPiece(window, pngOffsets)

