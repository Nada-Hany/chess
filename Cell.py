import Piece
import pygame

class cell:

    def __init__(self,x, y, pieceInCell : Piece.piece = None):
        self.x = x
        self.y = y
        self.pieceInCell = pieceInCell

    def setPiece(self, pieceInCell : Piece):
        self.pieceInCell = pieceInCell
    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    def drawPiece(self, window, pngOffset):
        window.blit(self.pieceInCell.image, (self.x + pngOffset, self.y + pngOffset))
    