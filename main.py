import pygame, Board
from game_events import *
from move_logic import *

pygame.font.init()

WIDTH, HEIGHT = 1200, 720
TILESIZE, TILENUMBER = 80, 8
X_OFFSET, Y_OFFSET = (WIDTH-(TILENUMBER*TILESIZE))//2, (HEIGHT-(TILENUMBER*TILESIZE))//2
PNGSIZE = 60
PNGOFFSETS = (TILESIZE-PNGSIZE)//2
BLACK, WHITE = (199, 121, 62), (255,255,255)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
board_obj = Board.board(TILENUMBER,BLACK,WHITE, TILESIZE, X_OFFSET, Y_OFFSET, WINDOW, WIDTH, HEIGHT)
board_obj.InitializePieces()
clock = pygame.time.Clock()
FPS = 60

while running:
   clock.tick(FPS)
   WINDOW.fill((90,50,30))
   board_obj.DrawBoard(WINDOW)
   board_obj.DrawPieces(WINDOW, PNGOFFSETS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
         position = pygame.mouse.get_pos()
         if(board_obj.gameOver == None and not board_obj.pawnPromotion):
            board_obj.HandlMovement(position)
         # checking gor pawn promotion selection
         elif (board_obj.gameOver == None and board_obj.pawnPromotion):
               
               HandlPromotionSelection(position, WIDTH//2-320//2, HEIGHT//2-80//2, 80, board_obj)
   if board_obj.pawnPromotion:
      DrawPossiblePromotion(WINDOW, board_obj.pawnToBePromoted.color, WIDTH, HEIGHT)
   if board_obj.gameOver == True:
      DrawGameOver(WINDOW, WIDTH, HEIGHT, "white wins!")
   elif board_obj.gameOver == False:
      DrawGameOver(WINDOW, WIDTH, HEIGHT, "black wins!")
   else:
      DrawPlayerTurn(WINDOW, WIDTH, board_obj.whiteTurn)
   pygame.display.flip()
  