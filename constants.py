import pygame
import mysql.connector
from db_connection import connectionCredentials
from screeninfo import get_monitors
pygame.init()

for m in get_monitors():
    if m.is_primary:
        HEIGHT = m.height
        WIDTH = m.width

BOARD_WIDTH = .6 * WIDTH
BOARD_HEIGHT = .8 * HEIGHT
SPACE_SIZE = BOARD_HEIGHT / 8;
MID_COLUMN_WIDTH = .30 * WIDTH

LG_PIECE_SIZE = SPACE_SIZE *.8
LG_PAWN_SIZE = SPACE_SIZE *.65
SM_PIECE_SIZE = ( MID_COLUMN_WIDTH / 2 ) * .25

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Data Persistent Two-Player Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
small_font = pygame.font.Font('freesansbold.ttf', 12)
pygame.font.init()

timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1.0, 0), (2.0, 0), (3.0, 0), (4.0, 0), (5.0, 0), (6.0, 0), (7.0, 0), (0.0, 1), (1.0, 1), (2.0, 1), (3.0, 1), (4.0, 1), (5.0, 1), (6.0, 1), (7.0, 1)]
white_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1.0, 7), (2.0, 7), (3.0, 7), (4.0, 7), (5.0, 7), (6.0, 7), (7.0, 7),(0, 6), (1.0, 6), (2.0, 6), (3.0, 6), (4.0, 6), (5.0, 6), (6.0, 6), (7.0, 6)]
black_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

# black king
black_king = pygame.transform.scale(pygame.image.load('assets/images/black/king2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
black_king_small = pygame.transform.scale(black_king, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white king
white_king = pygame.transform.scale(pygame.image.load('assets/images/white/king2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
white_king_small = pygame.transform.scale(white_king, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# black queen
black_queen = pygame.transform.scale(pygame.image.load('assets/images/black/queen2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
black_queen_small = pygame.transform.scale(black_queen, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white queen
white_queen = pygame.transform.scale(pygame.image.load('assets/images/white/queen2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
white_queen_small = pygame.transform.scale(white_queen, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# black rook
black_rook = pygame.transform.scale(pygame.image.load('assets/images/black/rook2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
black_rook_small = pygame.transform.scale(black_rook, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white rook
white_rook = pygame.transform.scale(pygame.image.load('assets/images/white/rook2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
white_rook_small = pygame.transform.scale(white_rook, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# black bishop
black_bishop = pygame.transform.scale(pygame.image.load('assets/images/black/bishop2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
black_bishop_small = pygame.transform.scale(black_bishop, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white bishop
white_bishop = pygame.transform.scale(pygame.image.load('assets/images/white/bishop2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
white_bishop_small = pygame.transform.scale(white_bishop, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# black knight
black_knight = pygame.transform.scale(pygame.image.load('assets/images/black/knight2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
black_knight_small = pygame.transform.scale(black_knight, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white pawn
white_knight = pygame.transform.scale(pygame.image.load('assets/images/white/knight2.png'), (LG_PIECE_SIZE, LG_PIECE_SIZE))
white_knight_small = pygame.transform.scale(white_knight, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# pawn
black_pawn = pygame.transform.scale(pygame.image.load('assets/images/black/pawn2.png'), (LG_PAWN_SIZE, LG_PAWN_SIZE))
black_pawn_small = pygame.transform.scale(black_pawn, (SM_PIECE_SIZE, SM_PIECE_SIZE))
# white pawn
white_pawn = pygame.transform.scale(pygame.image.load('assets/images/white/pawn2.png'), (LG_PAWN_SIZE, LG_PAWN_SIZE))
white_pawn_small = pygame.transform.scale(white_pawn, (SM_PIECE_SIZE, SM_PIECE_SIZE))

# text backgrounds
white_text_bg = pygame.transform.scale(pygame.image.load('assets/images/white/move-text-bg.png'), (300, SM_PIECE_SIZE))
black_text_bg = pygame.transform.scale(pygame.image.load('assets/images/black/move-text-bg.png'), (300, SM_PIECE_SIZE))

# white pieces
white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small,
                      white_bishop_small]
# black pieces
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small,
                      black_bishop_small]

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

mydb = mysql.connector.connect(host=connectionCredentials()[0], user=connectionCredentials()[1],password=connectionCredentials()[2], database=connectionCredentials()[3])
mycursor = mydb.cursor()
# INSERTS
create_new_game_sql = "INSERT INTO games (game_name, game_notes) VALUES (%s, %s)"
record_game_move_sql = "INSERT INTO gameMoves (games_id, order_number, color, piece, start_pos, end_pos) VALUES (%s, %s, %s, %s, %s, %s)"
record_game_over_sql = "INSERT INTO gamesCompleted (gameid, game_moves_id, winner, gameCompletedKey) VALUES(%s, %s, %s, %s)"
record_check_event_sql = "INSERT INTO gameChecks (king_color, king_pos, game_moves_id, gameCheckId) VALUES (%s, %s, %s, %s)"
record_castling_event_sql = "INSERT INTO gameCastling (color, rook_locations, king_pos, game_moves_id) VALUES (%s, %s, %s, %s)"
record_captures_sql = "INSERT INTO gameCaptures (captured_piece, game_moves_id, color, captured_id) VALUES (%s, %s, %s, %s)"
record_pawn_promotion_sql = "INSERT INTO gamePromotions (promotion_to_piece, game_moves_id, color, promotion_id) VALUES (%s, %s, %s, %s)"
# SELECTS
fetch_10_games_sql = "SELECT * FROM games ORDER BY id DESC LIMIT 10"
fetch_game_move_sql = "SELECT * FROM gameMoves WHERE games_id = %s AND order_number = %s"
fetch_game_moves_sql = "SELECT * FROM gameMoves WHERE games_id = %s"

white_promotions = ['bishop', 'knight', 'rook', 'queen']
black_promotions = ['bishop', 'knight', 'rook', 'queen']

# check variables/ flashing counter
counter = 0
moves_made_counter = 0
moves_made_list = []
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
promo_events = []
left_click = ""
check = False
check_events = []
white_in_check = False
black_in_check = False
gameid = 0
moveid = 0
turn_step = 0
# 0 - whites turn no selction: 1- whites turn piece selected: 2 - black turn no selection
selection = 100
valid_moves = []
captured_pieces_white = []
captured_pieces_black = []
previous_white_locations = []
previous_black_locations = []

all_moves = [
    'rook (0.0, 0.0)', 'rook (0.0, 1.0)', 'rook (0.0, 2.0)', 'rook (0.0, 3.0)', 'rook (0.0, 4.0)', 'rook (0.0, 5.0)', 'rook (0.0, 6.0)', 'rook (0.0, 7.0)', 
    'rook (1.0, 0.0)', 'rook (1.0, 1.0)', 'rook (1.0, 2.0)', 'rook (1.0, 3.0)', 'rook (1.0, 4.0)', 'rook (1.0, 5.0)', 'rook (1.0, 6.0)', 'rook (1.0, 7.0)', 
    'rook (2.0, 0.0)', 'rook (2.0, 1.0)', 'rook (2.0, 2.0)', 'rook (2.0, 3.0)', 'rook (2.0, 4.0)', 'rook (2.0, 5.0)', 'rook (2.0, 6.0)', 'rook (2.0, 7.0)', 
    'rook (3.0, 0.0)', 'rook (3.0, 1.0)', 'rook (3.0, 2.0)', 'rook (3.0, 3.0)', 'rook (3.0, 4.0)', 'rook (3.0, 5.0)', 'rook (3.0, 6.0)', 'rook (3.0, 7.0)', 
    'rook (4.0, 0.0)', 'rook (4.0, 1.0)', 'rook (4.0, 2.0)', 'rook (4.0, 3.0)', 'rook (4.0, 4.0)', 'rook (4.0, 5.0)', 'rook (4.0, 6.0)', 'rook (4.0, 7.0)', 
    'rook (5.0, 0.0)', 'rook (5.0, 1.0)', 'rook (5.0, 2.0)', 'rook (5.0, 3.0)', 'rook (5.0, 4.0)', 'rook (5.0, 5.0)', 'rook (5.0, 6.0)', 'rook (5.0, 7.0)', 
    'rook (6.0, 0.0)', 'rook (6.0, 1.0)', 'rook (6.0, 2.0)', 'rook (6.0, 3.0)', 'rook (6.0, 4.0)', 'rook (6.0, 5.0)', 'rook (6.0, 6.0)', 'rook (6.0, 7.0)', 
    'rook (7.0, 0.0)', 'rook (7.0, 1.0)', 'rook (7.0, 2.0)', 'rook (7.0, 3.0)', 'rook (7.0, 4.0)', 'rook (7.0, 5.0)', 'rook (7.0, 6.0)', 'rook (7.0, 7.0)',
    'knight (0.0, 0.0)', 'knight (0.0, 1.0)', 'knight (0.0, 2.0)', 'knight (0.0, 3.0)', 'knight (0.0, 4.0)', 'knight (0.0, 5.0)', 'knight (0.0, 6.0)', 'knight (0.0, 7.0)', 
    'knight (1.0, 0.0)', 'knight (1.0, 1.0)', 'knight (1.0, 2.0)', 'knight (1.0, 3.0)', 'knight (1.0, 4.0)', 'knight (1.0, 5.0)', 'knight (1.0, 6.0)', 'knight (1.0, 7.0)', 
    'knight (2.0, 0.0)', 'knight (2.0, 1.0)', 'knight (2.0, 2.0)', 'knight (2.0, 3.0)', 'knight (2.0, 4.0)', 'knight (2.0, 5.0)', 'knight (2.0, 6.0)', 'knight (2.0, 7.0)', 
    'knight (3.0, 0.0)', 'knight (3.0, 1.0)', 'knight (3.0, 2.0)', 'knight (3.0, 3.0)', 'knight (3.0, 4.0)', 'knight (3.0, 5.0)', 'knight (3.0, 6.0)', 'knight (3.0, 7.0)', 
    'knight (4.0, 0.0)', 'knight (4.0, 1.0)', 'knight (4.0, 2.0)', 'knight (4.0, 3.0)', 'knight (4.0, 4.0)', 'knight (4.0, 5.0)', 'knight (4.0, 6.0)', 'knight (4.0, 7.0)', 
    'knight (5.0, 0.0)', 'knight (5.0, 1.0)', 'knight (5.0, 2.0)', 'knight (5.0, 3.0)', 'knight (5.0, 4.0)', 'knight (5.0, 5.0)', 'knight (5.0, 6.0)', 'knight (5.0, 7.0)', 
    'knight (6.0, 0.0)', 'knight (6.0, 1.0)', 'knight (6.0, 2.0)', 'knight (6.0, 3.0)', 'knight (6.0, 4.0)', 'knight (6.0, 5.0)', 'knight (6.0, 6.0)', 'knight (6.0, 7.0)', 
    'knight (7.0, 0.0)', 'knight (7.0, 1.0)', 'knight (7.0, 2.0)', 'knight (7.0, 3.0)', 'knight (7.0, 4.0)', 'knight (7.0, 5.0)', 'knight (7.0, 6.0)', 'knight (7.0, 7.0)',
    'bishop (0.0, 0.0)', 'bishop (0.0, 1.0)', 'bishop (0.0, 2.0)', 'bishop (0.0, 3.0)', 'bishop (0.0, 4.0)', 'bishop (0.0, 5.0)', 'bishop (0.0, 6.0)', 'bishop (0.0, 7.0)', 
    'bishop (1.0, 0.0)', 'bishop (1.0, 1.0)', 'bishop (1.0, 2.0)', 'bishop (1.0, 3.0)', 'bishop (1.0, 4.0)', 'bishop (1.0, 5.0)', 'bishop (1.0, 6.0)', 'bishop (1.0, 7.0)', 
    'bishop (2.0, 0.0)', 'bishop (2.0, 1.0)', 'bishop (2.0, 2.0)', 'bishop (2.0, 3.0)', 'bishop (2.0, 4.0)', 'bishop (2.0, 5.0)', 'bishop (2.0, 6.0)', 'bishop (2.0, 7.0)', 
    'bishop (3.0, 0.0)', 'bishop (3.0, 1.0)', 'bishop (3.0, 2.0)', 'bishop (3.0, 3.0)', 'bishop (3.0, 4.0)', 'bishop (3.0, 5.0)', 'bishop (3.0, 6.0)', 'bishop (3.0, 7.0)', 
    'bishop (4.0, 0.0)', 'bishop (4.0, 1.0)', 'bishop (4.0, 2.0)', 'bishop (4.0, 3.0)', 'bishop (4.0, 4.0)', 'bishop (4.0, 5.0)', 'bishop (4.0, 6.0)', 'bishop (4.0, 7.0)', 
    'bishop (5.0, 0.0)', 'bishop (5.0, 1.0)', 'bishop (5.0, 2.0)', 'bishop (5.0, 3.0)', 'bishop (5.0, 4.0)', 'bishop (5.0, 5.0)', 'bishop (5.0, 6.0)', 'bishop (5.0, 7.0)', 
    'bishop (6.0, 0.0)', 'bishop (6.0, 1.0)', 'bishop (6.0, 2.0)', 'bishop (6.0, 3.0)', 'bishop (6.0, 4.0)', 'bishop (6.0, 5.0)', 'bishop (6.0, 6.0)', 'bishop (6.0, 7.0)', 
    'bishop (7.0, 0.0)', 'bishop (7.0, 1.0)', 'bishop (7.0, 2.0)', 'bishop (7.0, 3.0)', 'bishop (7.0, 4.0)', 'bishop (7.0, 5.0)', 'bishop (7.0, 6.0)', 'bishop (7.0, 7.0)',
    'king (0.0, 0.0)', 'king (0.0, 1.0)', 'king (0.0, 2.0)', 'king (0.0, 3.0)', 'king (0.0, 4.0)', 'king (0.0, 5.0)', 'king (0.0, 6.0)', 'king (0.0, 7.0)', 
    'king (1.0, 0.0)', 'king (1.0, 1.0)', 'king (1.0, 2.0)', 'king (1.0, 3.0)', 'king (1.0, 4.0)', 'king (1.0, 5.0)', 'king (1.0, 6.0)', 'king (1.0, 7.0)', 
    'king (2.0, 0.0)', 'king (2.0, 1.0)', 'king (2.0, 2.0)', 'king (2.0, 3.0)', 'king (2.0, 4.0)', 'king (2.0, 5.0)', 'king (2.0, 6.0)', 'king (2.0, 7.0)', 
    'king (3.0, 0.0)', 'king (3.0, 1.0)', 'king (3.0, 2.0)', 'king (3.0, 3.0)', 'king (3.0, 4.0)', 'king (3.0, 5.0)', 'king (3.0, 6.0)', 'king (3.0, 7.0)', 
    'king (4.0, 0.0)', 'king (4.0, 1.0)', 'king (4.0, 2.0)', 'king (4.0, 3.0)', 'king (4.0, 4.0)', 'king (4.0, 5.0)', 'king (4.0, 6.0)', 'king (4.0, 7.0)', 
    'king (5.0, 0.0)', 'king (5.0, 1.0)', 'king (5.0, 2.0)', 'king (5.0, 3.0)', 'king (5.0, 4.0)', 'king (5.0, 5.0)', 'king (5.0, 6.0)', 'king (5.0, 7.0)', 
    'king (6.0, 0.0)', 'king (6.0, 1.0)', 'king (6.0, 2.0)', 'king (6.0, 3.0)', 'king (6.0, 4.0)', 'king (6.0, 5.0)', 'king (6.0, 6.0)', 'king (6.0, 7.0)', 
    'king (7.0, 0.0)', 'king (7.0, 1.0)', 'king (7.0, 2.0)', 'king (7.0, 3.0)', 'king (7.0, 4.0)', 'king (7.0, 5.0)', 'king (7.0, 6.0)', 'king (7.0, 7.0)',
    'queen (0.0, 0.0)', 'queen (0.0, 1.0)', 'queen (0.0, 2.0)', 'queen (0.0, 3.0)', 'queen (0.0, 4.0)', 'queen (0.0, 5.0)', 'queen (0.0, 6.0)', 'queen (0.0, 7.0)', 
    'queen (1.0, 0.0)', 'queen (1.0, 1.0)', 'queen (1.0, 2.0)', 'queen (1.0, 3.0)', 'queen (1.0, 4.0)', 'queen (1.0, 5.0)', 'queen (1.0, 6.0)', 'queen (1.0, 7.0)', 
    'queen (2.0, 0.0)', 'queen (2.0, 1.0)', 'queen (2.0, 2.0)', 'queen (2.0, 3.0)', 'queen (2.0, 4.0)', 'queen (2.0, 5.0)', 'queen (2.0, 6.0)', 'queen (2.0, 7.0)', 
    'queen (3.0, 0.0)', 'queen (3.0, 1.0)', 'queen (3.0, 2.0)', 'queen (3.0, 3.0)', 'queen (3.0, 4.0)', 'queen (3.0, 5.0)', 'queen (3.0, 6.0)', 'queen (3.0, 7.0)', 
    'queen (4.0, 0.0)', 'queen (4.0, 1.0)', 'queen (4.0, 2.0)', 'queen (4.0, 3.0)', 'queen (4.0, 4.0)', 'queen (4.0, 5.0)', 'queen (4.0, 6.0)', 'queen (4.0, 7.0)', 
    'queen (5.0, 0.0)', 'queen (5.0, 1.0)', 'queen (5.0, 2.0)', 'queen (5.0, 3.0)', 'queen (5.0, 4.0)', 'queen (5.0, 5.0)', 'queen (5.0, 6.0)', 'queen (5.0, 7.0)', 
    'queen (6.0, 0.0)', 'queen (6.0, 1.0)', 'queen (6.0, 2.0)', 'queen (6.0, 3.0)', 'queen (6.0, 4.0)', 'queen (6.0, 5.0)', 'queen (6.0, 6.0)', 'queen (6.0, 7.0)', 
    'queen (7.0, 0.0)', 'queen (7.0, 1.0)', 'queen (7.0, 2.0)', 'queen (7.0, 3.0)', 'queen (7.0, 4.0)', 'queen (7.0, 5.0)', 'queen (7.0, 6.0)', 'queen (7.0, 7.0)',
    'pawn (0.0, 0.0)', 'pawn (0.0, 1.0)', 'pawn (0.0, 2.0)', 'pawn (0.0, 3.0)', 'pawn (0.0, 4.0)', 'pawn (0.0, 5.0)', 'pawn (0.0, 6.0)', 'pawn (0.0, 7.0)', 
    'pawn (1.0, 0.0)', 'pawn (1.0, 1.0)', 'pawn (1.0, 2.0)', 'pawn (1.0, 3.0)', 'pawn (1.0, 4.0)', 'pawn (1.0, 5.0)', 'pawn (1.0, 6.0)', 'pawn (1.0, 7.0)', 
    'pawn (2.0, 0.0)', 'pawn (2.0, 1.0)', 'pawn (2.0, 2.0)', 'pawn (2.0, 3.0)', 'pawn (2.0, 4.0)', 'pawn (2.0, 5.0)', 'pawn (2.0, 6.0)', 'pawn (2.0, 7.0)', 
    'pawn (3.0, 0.0)', 'pawn (3.0, 1.0)', 'pawn (3.0, 2.0)', 'pawn (3.0, 3.0)', 'pawn (3.0, 4.0)', 'pawn (3.0, 5.0)', 'pawn (3.0, 6.0)', 'pawn (3.0, 7.0)', 
    'pawn (4.0, 0.0)', 'pawn (4.0, 1.0)', 'pawn (4.0, 2.0)', 'pawn (4.0, 3.0)', 'pawn (4.0, 4.0)', 'pawn (4.0, 5.0)', 'pawn (4.0, 6.0)', 'pawn (4.0, 7.0)', 
    'pawn (5.0, 0.0)', 'pawn (5.0, 1.0)', 'pawn (5.0, 2.0)', 'pawn (5.0, 3.0)', 'pawn (5.0, 4.0)', 'pawn (5.0, 5.0)', 'pawn (5.0, 6.0)', 'pawn (5.0, 7.0)', 
    'pawn (6.0, 0.0)', 'pawn (6.0, 1.0)', 'pawn (6.0, 2.0)', 'pawn (6.0, 3.0)', 'pawn (6.0, 4.0)', 'pawn (6.0, 5.0)', 'pawn (6.0, 6.0)', 'pawn (6.0, 7.0)', 
    'pawn (7.0, 0.0)', 'pawn (7.0, 1.0)', 'pawn (7.0, 2.0)', 'pawn (7.0, 3.0)', 'pawn (7.0, 4.0)', 'pawn (7.0, 5.0)', 'pawn (7.0, 6.0)', 'pawn (7.0, 7.0)',
    'rook (0.0, 0.0)', 'rook (0.0, 1.0)', 'rook (0.0, 2.0)', 'rook (0.0, 3.0)', 'rook (0.0, 4.0)', 'rook (0.0, 5.0)', 'rook (0.0, 6.0)', 'rook (0.0, 7.0)', 
    'rook (1.0, 0.0)', 'rook (1.0, 1.0)', 'rook (1.0, 2.0)', 'rook (1.0, 3.0)', 'rook (1.0, 4.0)', 'rook (1.0, 5.0)', 'rook (1.0, 6.0)', 'rook (1.0, 7.0)', 
    'rook (2.0, 0.0)', 'rook (2.0, 1.0)', 'rook (2.0, 2.0)', 'rook (2.0, 3.0)', 'rook (2.0, 4.0)', 'rook (2.0, 5.0)', 'rook (2.0, 6.0)', 'rook (2.0, 7.0)', 
    'rook (3.0, 0.0)', 'rook (3.0, 1.0)', 'rook (3.0, 2.0)', 'rook (3.0, 3.0)', 'rook (3.0, 4.0)', 'rook (3.0, 5.0)', 'rook (3.0, 6.0)', 'rook (3.0, 7.0)', 
    'rook (4.0, 0.0)', 'rook (4.0, 1.0)', 'rook (4.0, 2.0)', 'rook (4.0, 3.0)', 'rook (4.0, 4.0)', 'rook (4.0, 5.0)', 'rook (4.0, 6.0)', 'rook (4.0, 7.0)', 
    'rook (5.0, 0.0)', 'rook (5.0, 1.0)', 'rook (5.0, 2.0)', 'rook (5.0, 3.0)', 'rook (5.0, 4.0)', 'rook (5.0, 5.0)', 'rook (5.0, 6.0)', 'rook (5.0, 7.0)', 
    'rook (6.0, 0.0)', 'rook (6.0, 1.0)', 'rook (6.0, 2.0)', 'rook (6.0, 3.0)', 'rook (6.0, 4.0)', 'rook (6.0, 5.0)', 'rook (6.0, 6.0)', 'rook (6.0, 7.0)', 
    'rook (7.0, 0.0)', 'rook (7.0, 1.0)', 'rook (7.0, 2.0)', 'rook (7.0, 3.0)', 'rook (7.0, 4.0)', 'rook (7.0, 5.0)', 'rook (7.0, 6.0)', 'rook (7.0, 7.0)',
    'knight (0.0, 0.0)', 'knight (0.0, 1.0)', 'knight (0.0, 2.0)', 'knight (0.0, 3.0)', 'knight (0.0, 4.0)', 'knight (0.0, 5.0)', 'knight (0.0, 6.0)', 'knight (0.0, 7.0)', 
    'knight (1.0, 0.0)', 'knight (1.0, 1.0)', 'knight (1.0, 2.0)', 'knight (1.0, 3.0)', 'knight (1.0, 4.0)', 'knight (1.0, 5.0)', 'knight (1.0, 6.0)', 'knight (1.0, 7.0)', 
    'knight (2.0, 0.0)', 'knight (2.0, 1.0)', 'knight (2.0, 2.0)', 'knight (2.0, 3.0)', 'knight (2.0, 4.0)', 'knight (2.0, 5.0)', 'knight (2.0, 6.0)', 'knight (2.0, 7.0)', 
    'knight (3.0, 0.0)', 'knight (3.0, 1.0)', 'knight (3.0, 2.0)', 'knight (3.0, 3.0)', 'knight (3.0, 4.0)', 'knight (3.0, 5.0)', 'knight (3.0, 6.0)', 'knight (3.0, 7.0)', 
    'knight (4.0, 0.0)', 'knight (4.0, 1.0)', 'knight (4.0, 2.0)', 'knight (4.0, 3.0)', 'knight (4.0, 4.0)', 'knight (4.0, 5.0)', 'knight (4.0, 6.0)', 'knight (4.0, 7.0)', 
    'knight (5.0, 0.0)', 'knight (5.0, 1.0)', 'knight (5.0, 2.0)', 'knight (5.0, 3.0)', 'knight (5.0, 4.0)', 'knight (5.0, 5.0)', 'knight (5.0, 6.0)', 'knight (5.0, 7.0)', 
    'knight (6.0, 0.0)', 'knight (6.0, 1.0)', 'knight (6.0, 2.0)', 'knight (6.0, 3.0)', 'knight (6.0, 4.0)', 'knight (6.0, 5.0)', 'knight (6.0, 6.0)', 'knight (6.0, 7.0)', 
    'knight (7.0, 0.0)', 'knight (7.0, 1.0)', 'knight (7.0, 2.0)', 'knight (7.0, 3.0)', 'knight (7.0, 4.0)', 'knight (7.0, 5.0)', 'knight (7.0, 6.0)', 'knight (7.0, 7.0)',
    'bishop (0.0, 0.0)', 'bishop (0.0, 1.0)', 'bishop (0.0, 2.0)', 'bishop (0.0, 3.0)', 'bishop (0.0, 4.0)', 'bishop (0.0, 5.0)', 'bishop (0.0, 6.0)', 'bishop (0.0, 7.0)', 
    'bishop (1.0, 0.0)', 'bishop (1.0, 1.0)', 'bishop (1.0, 2.0)', 'bishop (1.0, 3.0)', 'bishop (1.0, 4.0)', 'bishop (1.0, 5.0)', 'bishop (1.0, 6.0)', 'bishop (1.0, 7.0)', 
    'bishop (2.0, 0.0)', 'bishop (2.0, 1.0)', 'bishop (2.0, 2.0)', 'bishop (2.0, 3.0)', 'bishop (2.0, 4.0)', 'bishop (2.0, 5.0)', 'bishop (2.0, 6.0)', 'bishop (2.0, 7.0)', 
    'bishop (3.0, 0.0)', 'bishop (3.0, 1.0)', 'bishop (3.0, 2.0)', 'bishop (3.0, 3.0)', 'bishop (3.0, 4.0)', 'bishop (3.0, 5.0)', 'bishop (3.0, 6.0)', 'bishop (3.0, 7.0)', 
    'bishop (4.0, 0.0)', 'bishop (4.0, 1.0)', 'bishop (4.0, 2.0)', 'bishop (4.0, 3.0)', 'bishop (4.0, 4.0)', 'bishop (4.0, 5.0)', 'bishop (4.0, 6.0)', 'bishop (4.0, 7.0)', 
    'bishop (5.0, 0.0)', 'bishop (5.0, 1.0)', 'bishop (5.0, 2.0)', 'bishop (5.0, 3.0)', 'bishop (5.0, 4.0)', 'bishop (5.0, 5.0)', 'bishop (5.0, 6.0)', 'bishop (5.0, 7.0)', 
    'bishop (6.0, 0.0)', 'bishop (6.0, 1.0)', 'bishop (6.0, 2.0)', 'bishop (6.0, 3.0)', 'bishop (6.0, 4.0)', 'bishop (6.0, 5.0)', 'bishop (6.0, 6.0)', 'bishop (6.0, 7.0)', 
    'bishop (7.0, 0.0)', 'bishop (7.0, 1.0)', 'bishop (7.0, 2.0)', 'bishop (7.0, 3.0)', 'bishop (7.0, 4.0)', 'bishop (7.0, 5.0)', 'bishop (7.0, 6.0)', 'bishop (7.0, 7.0)',
    'king (0.0, 0.0)', 'king (0.0, 1.0)', 'king (0.0, 2.0)', 'king (0.0, 3.0)', 'king (0.0, 4.0)', 'king (0.0, 5.0)', 'king (0.0, 6.0)', 'king (0.0, 7.0)', 
    'king (1.0, 0.0)', 'king (1.0, 1.0)', 'king (1.0, 2.0)', 'king (1.0, 3.0)', 'king (1.0, 4.0)', 'king (1.0, 5.0)', 'king (1.0, 6.0)', 'king (1.0, 7.0)', 
    'king (2.0, 0.0)', 'king (2.0, 1.0)', 'king (2.0, 2.0)', 'king (2.0, 3.0)', 'king (2.0, 4.0)', 'king (2.0, 5.0)', 'king (2.0, 6.0)', 'king (2.0, 7.0)', 
    'king (3.0, 0.0)', 'king (3.0, 1.0)', 'king (3.0, 2.0)', 'king (3.0, 3.0)', 'king (3.0, 4.0)', 'king (3.0, 5.0)', 'king (3.0, 6.0)', 'king (3.0, 7.0)', 
    'king (4.0, 0.0)', 'king (4.0, 1.0)', 'king (4.0, 2.0)', 'king (4.0, 3.0)', 'king (4.0, 4.0)', 'king (4.0, 5.0)', 'king (4.0, 6.0)', 'king (4.0, 7.0)', 
    'king (5.0, 0.0)', 'king (5.0, 1.0)', 'king (5.0, 2.0)', 'king (5.0, 3.0)', 'king (5.0, 4.0)', 'king (5.0, 5.0)', 'king (5.0, 6.0)', 'king (5.0, 7.0)', 
    'king (6.0, 0.0)', 'king (6.0, 1.0)', 'king (6.0, 2.0)', 'king (6.0, 3.0)', 'king (6.0, 4.0)', 'king (6.0, 5.0)', 'king (6.0, 6.0)', 'king (6.0, 7.0)', 
    'king (7.0, 0.0)', 'king (7.0, 1.0)', 'king (7.0, 2.0)', 'king (7.0, 3.0)', 'king (7.0, 4.0)', 'king (7.0, 5.0)', 'king (7.0, 6.0)', 'king (7.0, 7.0)',
    'queen (0.0, 0.0)', 'queen (0.0, 1.0)', 'queen (0.0, 2.0)', 'queen (0.0, 3.0)', 'queen (0.0, 4.0)', 'queen (0.0, 5.0)', 'queen (0.0, 6.0)', 'queen (0.0, 7.0)', 
    'queen (1.0, 0.0)', 'queen (1.0, 1.0)', 'queen (1.0, 2.0)', 'queen (1.0, 3.0)', 'queen (1.0, 4.0)', 'queen (1.0, 5.0)', 'queen (1.0, 6.0)', 'queen (1.0, 7.0)', 
    'queen (2.0, 0.0)', 'queen (2.0, 1.0)', 'queen (2.0, 2.0)', 'queen (2.0, 3.0)', 'queen (2.0, 4.0)', 'queen (2.0, 5.0)', 'queen (2.0, 6.0)', 'queen (2.0, 7.0)', 
    'queen (3.0, 0.0)', 'queen (3.0, 1.0)', 'queen (3.0, 2.0)', 'queen (3.0, 3.0)', 'queen (3.0, 4.0)', 'queen (3.0, 5.0)', 'queen (3.0, 6.0)', 'queen (3.0, 7.0)', 
    'queen (4.0, 0.0)', 'queen (4.0, 1.0)', 'queen (4.0, 2.0)', 'queen (4.0, 3.0)', 'queen (4.0, 4.0)', 'queen (4.0, 5.0)', 'queen (4.0, 6.0)', 'queen (4.0, 7.0)', 
    'queen (5.0, 0.0)', 'queen (5.0, 1.0)', 'queen (5.0, 2.0)', 'queen (5.0, 3.0)', 'queen (5.0, 4.0)', 'queen (5.0, 5.0)', 'queen (5.0, 6.0)', 'queen (5.0, 7.0)', 
    'queen (6.0, 0.0)', 'queen (6.0, 1.0)', 'queen (6.0, 2.0)', 'queen (6.0, 3.0)', 'queen (6.0, 4.0)', 'queen (6.0, 5.0)', 'queen (6.0, 6.0)', 'queen (6.0, 7.0)', 
    'queen (7.0, 0.0)', 'queen (7.0, 1.0)', 'queen (7.0, 2.0)', 'queen (7.0, 3.0)', 'queen (7.0, 4.0)', 'queen (7.0, 5.0)', 'queen (7.0, 6.0)', 'queen (7.0, 7.0)',
    'pawn (0.0, 0.0)', 'pawn (0.0, 1.0)', 'pawn (0.0, 2.0)', 'pawn (0.0, 3.0)', 'pawn (0.0, 4.0)', 'pawn (0.0, 5.0)', 'pawn (0.0, 6.0)', 'pawn (0.0, 7.0)', 
    'pawn (1.0, 0.0)', 'pawn (1.0, 1.0)', 'pawn (1.0, 2.0)', 'pawn (1.0, 3.0)', 'pawn (1.0, 4.0)', 'pawn (1.0, 5.0)', 'pawn (1.0, 6.0)', 'pawn (1.0, 7.0)', 
    'pawn (2.0, 0.0)', 'pawn (2.0, 1.0)', 'pawn (2.0, 2.0)', 'pawn (2.0, 3.0)', 'pawn (2.0, 4.0)', 'pawn (2.0, 5.0)', 'pawn (2.0, 6.0)', 'pawn (2.0, 7.0)', 
    'pawn (3.0, 0.0)', 'pawn (3.0, 1.0)', 'pawn (3.0, 2.0)', 'pawn (3.0, 3.0)', 'pawn (3.0, 4.0)', 'pawn (3.0, 5.0)', 'pawn (3.0, 6.0)', 'pawn (3.0, 7.0)', 
    'pawn (4.0, 0.0)', 'pawn (4.0, 1.0)', 'pawn (4.0, 2.0)', 'pawn (4.0, 3.0)', 'pawn (4.0, 4.0)', 'pawn (4.0, 5.0)', 'pawn (4.0, 6.0)', 'pawn (4.0, 7.0)', 
    'pawn (5.0, 0.0)', 'pawn (5.0, 1.0)', 'pawn (5.0, 2.0)', 'pawn (5.0, 3.0)', 'pawn (5.0, 4.0)', 'pawn (5.0, 5.0)', 'pawn (5.0, 6.0)', 'pawn (5.0, 7.0)', 
    'pawn (6.0, 0.0)', 'pawn (6.0, 1.0)', 'pawn (6.0, 2.0)', 'pawn (6.0, 3.0)', 'pawn (6.0, 4.0)', 'pawn (6.0, 5.0)', 'pawn (6.0, 6.0)', 'pawn (6.0, 7.0)', 
    'pawn (7.0, 0.0)', 'pawn (7.0, 1.0)', 'pawn (7.0, 2.0)', 'pawn (7.0, 3.0)', 'pawn (7.0, 4.0)', 'pawn (7.0, 5.0)', 'pawn (7.0, 6.0)', 'pawn (7.0, 7.0)',
    'castle (0.0, 0.0) (1.0, 0.0)', 'castle (2.0, 0.0) (1.0, 0.0)', 'castle (2.0, 7.0) (1.0, 7.0)', 'castle (4.0, 7.0) (5.0, 7.0)', 'castle (4.0, 0.0) (5.0, 0.0)',
    'castle (0.0, 7.0) (1.0, 7.0)', 'castle (7.0, 0.0) (5.0, 0.0)', 'castle (7.0, 7.0) (5.0, 7.0)']
