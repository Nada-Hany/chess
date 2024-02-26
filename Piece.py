import Enums
class piece:
    moved = False
    king_can_castle_left = False
    rook_can_castle = False
    def __init__(self, color:Enums.Color, type, isAlive = True, isSelected = False, image = None):
        self.color = color
        self.isAlive = isAlive
        self.isSelected = isSelected
        self.type = type 
        self.image = image
        self.previousX = -1
        self.previousY = -1
    
    def FirstMove(self):
        self.moved = True

    def Die(self, blackList, whiteList, cells, x, y):
        cells[y][x].pieceInCell = None
        if(self.color == Enums.Color.BLACK):
            blackList.append(self)
        else:
            whiteList.append(self)
            
