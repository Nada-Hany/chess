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

moves[Enums.PieceType.BISHOP]

while(gameStatus == Enums.GameState.RUNNING):
    WINDOW.fill((0,0,0))
    board_obj.DrawBoard(WINDOW)
    board_obj.drawPieces(WINDOW, PNGOFFSETS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameStatus = Enums.GameState.NOTRUNNING
      if event.type == pygame.MOUSEBUTTONUP:
         position = pygame.mouse.get_pos()
         board_obj.handlMovement(position)
    pygame.display.update()
  

         

   