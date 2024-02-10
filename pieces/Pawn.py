from pieces import Piece
class pawn(Piece.piece):

    def __init__(self, color, isAlive, isSelected, x, y):
        super().__init__(color, isAlive, isSelected, x, y)
    
    def move(self):
        pass
    
    def canMove(self, x, y):
        pass