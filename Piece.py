import Enums
class piece:
    def __init__(self, color:Enums.Color, type, isAlive = True, isSelected = False, image = None):
        self.color = color
        self.isAlive = isAlive
        self.isSelected = isSelected
        self.type = type 
        self.image = image
        self.previousX = -1
        self.previousY = -1    
        self.moved = False
        self.canCastle = False
        self.possibleMoves = []

        self.leftRookCastleX = 3
        self.rightRookCastleX = 5
        self.kingCastleRightX = 6
        self.kingCastleLeftX = 2
        self.initialX = -1
        self.initialY = -1

    def SetInitialCor(self, x, y):
        self.initialX = x
        self.initialY = y

    def Moved(self):
        self.moved = True

    def Die(self, blackList, whiteList, cells, x, y):
        cells[y][x].pieceInCell = None
        if(self.color == Enums.Color.BLACK):
            blackList.append(self)
        else:
            whiteList.append(self)
            
