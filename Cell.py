import Piece
class cell:

    def __init__(self,x, y, pieceInCell : Piece.piece = None):
        self.x = x
        self.y = y
        self.pieceInCell = pieceInCell

    def SetPiece(self, pieceInCell : Piece):
        self.pieceInCell = pieceInCell
    def SetXY(self, x, y):
        self.x = x
        self.y = y
    
    def DrawPiece(self, window, pngOffset):
        window.blit(self.pieceInCell.image, (self.x + pngOffset, self.y + pngOffset))
    