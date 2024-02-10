class piece:

    def __init__(self, color, isAlive, isSelected, x, y):
        self.color = color
        self.isAlive = isAlive
        self.isSelected = isSelected
        self.x = x
        self.y = y
    
    def move(self):
        pass
    
    def canMove(self, x, y):
        pass
