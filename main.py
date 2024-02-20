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
board_obj.InitializePieces()

while(gameStatus == Enums.GameState.RUNNING):
   WINDOW.fill((90,50,30))
   board_obj.DrawBoard(WINDOW)
   board_obj.DrawPieces(WINDOW, PNGOFFSETS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameStatus = Enums.GameState.NOTRUNNING
      if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
         position = pygame.mouse.get_pos()
         board_obj.HandlMovement(position)
   pygame.display.update()
  

         

   