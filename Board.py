import Enums, Piece
import pygame
class board:
 
    def __init__(self, tilesNumber, color1, color2, tileSize, ):
        self.tilesNumber = tilesNumber
        self.color1 = color1
        self.color2 = color2
        self.tileSize = tileSize
    def DrawBoard(self, window, leftSpace, topSpace):

        for i in range(self.tilesNumber):
            for g in range(self.tilesNumber):
                if((i%2==0 and g%2==0) or i==g or (i%2!=0 and g%2!=0)):
                    pygame.draw.rect(window, self.color1, (g*self.tileSize +leftSpace, i*self.tileSize+topSpace,self.tileSize, self.tileSize))
                else:
                    pygame.draw.rect(window, self.color2, (g*self.tileSize +leftSpace, i*self.tileSize+topSpace,self.tileSize, self.tileSize))


               
