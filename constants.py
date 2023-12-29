import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_moved = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
captured_pieces_white = []
captured_pieces_black = []
turn_step = 0
# 0 - whites turn no selction: 1- whites turn piece selected: 2 - black turn no selection
selection = 100
valid_moves = []
# load in game piece images (queen, king, rook, bishop, knight, pawn) * 2

# kings ############
# black king
black_king = pygame.transform.scale(pygame.image.load('assets/images/black/king.png'), (80, 80))
black_king_small = pygame.transform.scale(black_king, (45, 45))
# white king
white_king = pygame.transform.scale(pygame.image.load('assets/images/white/king.png'), (80, 80))
white_king_small = pygame.transform.scale(white_king, (45, 45))

# queens ###########
# black queen
black_queen = pygame.transform.scale(pygame.image.load('assets/images/black/queen.png'), (80, 80))
black_queen_small = pygame.transform.scale(black_queen, (45, 45))
# white queen
white_queen = pygame.transform.scale(pygame.image.load('assets/images/white/queen.png'), (80, 80))
white_queen_small = pygame.transform.scale(white_queen, (45, 45))

# rooks ###########
# black rook
black_rook = pygame.transform.scale(pygame.image.load('assets/images/black/rook.png'), (80, 80))
black_rook_small = pygame.transform.scale(black_rook, (45, 45))
# white rook
white_rook = pygame.transform.scale(pygame.image.load('assets/images/white/rook.png'), (80, 80))
white_rook_small = pygame.transform.scale(white_rook, (45, 45))

# bishops ##########
# black bishop
black_bishop = pygame.transform.scale(pygame.image.load('assets/images/black/bishop.png'), (80, 80))
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))
# white bishop
white_bishop = pygame.transform.scale(pygame.image.load('assets/images/white/bishop.png'), (80, 80))
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))

# knights ##########
# black knight
black_knight = pygame.transform.scale(pygame.image.load('assets/images/black/knight.png'), (80, 80))
black_knight_small = pygame.transform.scale(black_knight, (45, 45))
# white knight
white_knight = pygame.transform.scale(pygame.image.load('assets/images/white/knight.png'), (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

# pawns ##########
# black pawn
black_pawn = pygame.transform.scale(pygame.image.load('assets/images/black/pawn.png'), (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
# white pawn
white_pawn = pygame.transform.scale(pygame.image.load('assets/images/white/pawn.png'), (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# white pieces
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small,
                      white_bishop_small]
# black pieces
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small,
                      black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

white_promotions = ['bishop', 'knight', 'rook', 'queen']
black_promotions = ['bishop', 'knight', 'rook', 'queen']
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
left_click = ""