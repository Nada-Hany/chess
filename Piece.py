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
    
    # def canMove(self, x, y):
    #     pass
    def getType(self):
        return self.type
    def GotSelected(self, blackList, whiteList, cells, x, y):
        if(self.isSelected == False):
            # showing all possible moves
            self.isSelected = True
        else:
            print("true")
            # self.isSelected = False
            # self.isAlive = False
            # self.Die(blackList, whiteList, cells, x, y)
    
    def Die(self, blackList, whiteList, cells, x, y):
        cells[y][x].pieceInCell = None
        if(self.color == Enums.Color.BLACK):
            blackList.append(self)
        else:
            whiteList.append(self)
        # cells.remove(self)
        print(whiteList)
        print(blackList)
            
