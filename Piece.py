import Enums, os, pygame
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
        self.checkMate = False
        self.possibleMoves = []
        self.invalidMoves = []
        self.leftRookCastleX = 3
        self.rightRookCastleX = 5
        self.kingCastleRightX = 6
        self.kingCastleLeftX = 2
        self.initialX = -1
        self.initialY = -1

    def SetInitialCor(self, x, y):
        self.initialX = x
        self.initialY = y

    def SetBasicsForPromotion(self, color:Enums.Color, type:Enums.PieceType):
        self.color = color
        self.type = type
        self.PromotePawn[type]

    def Moved(self):
        self.moved = True

    def Die(self, blackList, whiteList, cells, x, y):
        cells[y][x].pieceInCell = None
        if(self.color == Enums.Color.BLACK):
            blackList.append(self)
        else:
            whiteList.append(self)
            
    def SetBasicsForPromotion(self, color:Enums.Color, type:Enums.PieceType):
        self.color = color
        self.type = type
        self.PromotePawn[type]

    def SetBishop(self, color):
        BISHOP = Enums.PieceType.BISHOP

        self.type = BISHOP
        if(color == Enums.Color.BLACK):
            black_bishp_img = pygame.image.load(os.path.join('assets','black-bishop.png'))
            self.image = black_bishp_img
        else:
            white_bishp_img = pygame.image.load(os.path.join('assets','white-bishop.png'))
            self.image = white_bishp_img

    def SetRook(self, color):
        ROOK = Enums.PieceType.ROOK

        self.type = ROOK
        if(color == Enums.Color.BLACK):
            black_rook_img = pygame.image.load(os.path.join('assets','black-rook.png'))
            self.image = black_rook_img
        else:
            white_rook_img = pygame.image.load(os.path.join('assets','white-rook.png'))
            self.image = white_rook_img

    def SetQueen(self, color):
        QUEEN = Enums.PieceType.QUEEN

        self.type = QUEEN
        if(color == Enums.Color.BLACK):
            black_queen_img = pygame.image.load(os.path.join('assets','black-queen.png'))
            self.image = black_queen_img
        else:
            white_queen_img = pygame.image.load(os.path.join('assets','white-queen.png'))
            self.image = white_queen_img

    def SetKnight(self, color):
        KNIGHT = Enums.PieceType.KNIGHT

        self.type = KNIGHT
        if(color == Enums.Color.BLACK):
            black_knight_img = pygame.image.load(os.path.join('assets','black-knight.png'))
            self.image = black_knight_img
        else:
            white_knight_img = pygame.image.load(os.path.join('assets','white-knight.png'))
            self.image = white_knight_img

    PromotePawn={
        Enums.PieceType.BISHOP : SetBishop,
        Enums.PieceType.QUEEN : SetQueen,
        Enums.PieceType.KNIGHT : SetKnight,
        Enums.PieceType.ROOK : SetRook
    }
