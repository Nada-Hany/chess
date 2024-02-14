import pygame
import Board, Enums, Piece

WIDTH, HEIGHT = 1200, 720
TILESIZE, TILENUMBER = 80, 8
LEFT_SPACE, TOP_SPACE = (WIDTH-(TILENUMBER*TILESIZE))//2, (HEIGHT-(TILENUMBER*TILESIZE))//2
BLACK, WHITE = (199, 121, 62), (255,255,255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

isRunning = True
board_obj = Board.board(TILENUMBER,BLACK,WHITE, TILESIZE)
board_obj.DrawBoard(WINDOW, LEFT_SPACE, TOP_SPACE)   

while(isRunning):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         isRunning = False
    pygame.display.update()
  
         

   