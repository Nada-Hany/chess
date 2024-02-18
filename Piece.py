import Enums
class piece:

    def __init__(self, color:Enums.Color, isAlive, isSelected, type:Enums.PieceType, image = None):
        self.color = color
        self.isAlive = isAlive
        self.isSelected = isSelected
        self.type = type 
        self.image = image
    
    def move(self):
        pass
    def getType(self):
        return self.type.name
    def getColor (self):
        return self.color.name
    
    # def canMove(self, x, y):
    #     pass
