import pygame
import Board, Enums, Piece, Cell
from move_logic import *
WIDTH, HEIGHT = 1200, 720
TILESIZE, TILENUMBER = 80, 8
X_OFFSET, Y_OFFSET = (WIDTH-(TILENUMBER*TILESIZE))//2, (HEIGHT-(TILENUMBER*TILESIZE))//2
PNGSIZE = 60
PNGOFFSETS = (TILESIZE-PNGSIZE)//2
BLACK, WHITE = (199, 121, 62), (255,255,255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

gameStatus = Enums.GameState.RUNNING
board_obj = Board.board(TILENUMBER,BLACK,WHITE, TILESIZE, X_OFFSET, Y_OFFSET)
board_obj.DrawBoard(WINDOW)   

# for cell in board_obj.cells:
#    for eachCell in cell:
#       if(eachCell.pieceInCell != None):
#         print(eachCell.pieceInCell.getType() , eachCell.pieceInCell.getColor())
board_obj.drawPieces(WINDOW, PNGOFFSETS)
while(gameStatus == Enums.GameState.RUNNING):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameStatus = Enums.GameState.NOTRUNNING
    
    pygame.display.update()
  
         

   