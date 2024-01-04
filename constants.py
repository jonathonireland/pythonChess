import pygame
pygame.init()

WIDTH = 1300
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
small_font = pygame.font.Font('freesansbold.ttf', 8)
pygame.font.init()

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

all_white = ['white rook (0, 0)', 'white rook (0, 1)', 'white rook (0, 2)', 'white rook (0, 3)', 'white rook (0, 4)', 'white rook (0, 5)', 'white rook (0, 6)', 'white rook (0, 7)', 
    'white rook (1, 0)', 'white rook (1, 1)', 'white rook (1, 2)', 'white rook (1, 3)', 'white rook (1, 4)', 'white rook (1, 5)', 'white rook (1, 6)', 'white rook (1, 7)', 
    'white rook (2, 0)', 'white rook (2, 1)', 'white rook (2, 2)', 'white rook (2, 3)', 'white rook (2, 4)', 'white rook (2, 5)', 'white rook (2, 6)', 'white rook (2, 7)', 
    'white rook (3, 0)', 'white rook (3, 1)', 'white rook (3, 2)', 'white rook (3, 3)', 'white rook (3, 4)', 'white rook (3, 5)', 'white rook (3, 6)', 'white rook (3, 7)', 
    'white rook (4, 0)', 'white rook (4, 1)', 'white rook (4, 2)', 'white rook (4, 3)', 'white rook (4, 4)', 'white rook (4, 5)', 'white rook (4, 6)', 'white rook (4, 7)', 
    'white rook (5, 0)', 'white rook (5, 1)', 'white rook (5, 2)', 'white rook (5, 3)', 'white rook (5, 4)', 'white rook (5, 5)', 'white rook (5, 6)', 'white rook (5, 7)', 
    'white rook (6, 0)', 'white rook (6, 1)', 'white rook (6, 2)', 'white rook (6, 3)', 'white rook (6, 4)', 'white rook (6, 5)', 'white rook (6, 6)', 'white rook (6, 7)', 
    'white rook (7, 0)', 'white rook (7, 1)', 'white rook (7, 2)', 'white rook (7, 3)', 'white rook (7, 4)', 'white rook (7, 5)', 'white rook (7, 6)', 'white rook (7, 7)',
    'white knight (0, 0)', 'white knight (0, 1)', 'white knight (0, 2)', 'white knight (0, 3)', 'white knight (0, 4)', 'white knight (0, 5)', 'white knight (0, 6)', 'white knight (0, 7)', 
    'white knight (1, 0)', 'white knight (1, 1)', 'white knight (1, 2)', 'white knight (1, 3)', 'white knight (1, 4)', 'white knight (1, 5)', 'white knight (1, 6)', 'white knight (1, 7)', 
    'white knight (2, 0)', 'white knight (2, 1)', 'white knight (2, 2)', 'white knight (2, 3)', 'white knight (2, 4)', 'white knight (2, 5)', 'white knight (2, 6)', 'white knight (2, 7)', 
    'white knight (3, 0)', 'white knight (3, 1)', 'white knight (3, 2)', 'white knight (3, 3)', 'white knight (3, 4)', 'white knight (3, 5)', 'white knight (3, 6)', 'white knight (3, 7)', 
    'white knight (4, 0)', 'white knight (4, 1)', 'white knight (4, 2)', 'white knight (4, 3)', 'white knight (4, 4)', 'white knight (4, 5)', 'white knight (4, 6)', 'white knight (4, 7)', 
    'white knight (5, 0)', 'white knight (5, 1)', 'white knight (5, 2)', 'white knight (5, 3)', 'white knight (5, 4)', 'white knight (5, 5)', 'white knight (5, 6)', 'white knight (5, 7)', 
    'white knight (6, 0)', 'white knight (6, 1)', 'white knight (6, 2)', 'white knight (6, 3)', 'white knight (6, 4)', 'white knight (6, 5)', 'white knight (6, 6)', 'white knight (6, 7)', 
    'white knight (7, 0)', 'white knight (7, 1)', 'white knight (7, 2)', 'white knight (7, 3)', 'white knight (7, 4)', 'white knight (7, 5)', 'white knight (7, 6)', 'white knight (7, 7)',
    'white bishop (0, 0)', 'white bishop (0, 1)', 'white bishop (0, 2)', 'white bishop (0, 3)', 'white bishop (0, 4)', 'white bishop (0, 5)', 'white bishop (0, 6)', 'white bishop (0, 7)', 
    'white bishop (1, 0)', 'white bishop (1, 1)', 'white bishop (1, 2)', 'white bishop (1, 3)', 'white bishop (1, 4)', 'white bishop (1, 5)', 'white bishop (1, 6)', 'white bishop (1, 7)', 
    'white bishop (2, 0)', 'white bishop (2, 1)', 'white bishop (2, 2)', 'white bishop (2, 3)', 'white bishop (2, 4)', 'white bishop (2, 5)', 'white bishop (2, 6)', 'white bishop (2, 7)', 
    'white bishop (3, 0)', 'white bishop (3, 1)', 'white bishop (3, 2)', 'white bishop (3, 3)', 'white bishop (3, 4)', 'white bishop (3, 5)', 'white bishop (3, 6)', 'white bishop (3, 7)', 
    'white bishop (4, 0)', 'white bishop (4, 1)', 'white bishop (4, 2)', 'white bishop (4, 3)', 'white bishop (4, 4)', 'white bishop (4, 5)', 'white bishop (4, 6)', 'white bishop (4, 7)', 
    'white bishop (5, 0)', 'white bishop (5, 1)', 'white bishop (5, 2)', 'white bishop (5, 3)', 'white bishop (5, 4)', 'white bishop (5, 5)', 'white bishop (5, 6)', 'white bishop (5, 7)', 
    'white bishop (6, 0)', 'white bishop (6, 1)', 'white bishop (6, 2)', 'white bishop (6, 3)', 'white bishop (6, 4)', 'white bishop (6, 5)', 'white bishop (6, 6)', 'white bishop (6, 7)', 
    'white bishop (7, 0)', 'white bishop (7, 1)', 'white bishop (7, 2)', 'white bishop (7, 3)', 'white bishop (7, 4)', 'white bishop (7, 5)', 'white bishop (7, 6)', 'white bishop (7, 7)',
    'white king (0, 0)', 'white king (0, 1)', 'white king (0, 2)', 'white king (0, 3)', 'white king (0, 4)', 'white king (0, 5)', 'white king (0, 6)', 'white king (0, 7)', 
    'white king (1, 0)', 'white king (1, 1)', 'white king (1, 2)', 'white king (1, 3)', 'white king (1, 4)', 'white king (1, 5)', 'white king (1, 6)', 'white king (1, 7)', 
    'white king (2, 0)', 'white king (2, 1)', 'white king (2, 2)', 'white king (2, 3)', 'white king (2, 4)', 'white king (2, 5)', 'white king (2, 6)', 'white king (2, 7)', 
    'white king (3, 0)', 'white king (3, 1)', 'white king (3, 2)', 'white king (3, 3)', 'white king (3, 4)', 'white king (3, 5)', 'white king (3, 6)', 'white king (3, 7)', 
    'white king (4, 0)', 'white king (4, 1)', 'white king (4, 2)', 'white king (4, 3)', 'white king (4, 4)', 'white king (4, 5)', 'white king (4, 6)', 'white king (4, 7)', 
    'white king (5, 0)', 'white king (5, 1)', 'white king (5, 2)', 'white king (5, 3)', 'white king (5, 4)', 'white king (5, 5)', 'white king (5, 6)', 'white king (5, 7)', 
    'white king (6, 0)', 'white king (6, 1)', 'white king (6, 2)', 'white king (6, 3)', 'white king (6, 4)', 'white king (6, 5)', 'white king (6, 6)', 'white king (6, 7)', 
    'white king (7, 0)', 'white king (7, 1)', 'white king (7, 2)', 'white king (7, 3)', 'white king (7, 4)', 'white king (7, 5)', 'white king (7, 6)', 'white king (7, 7)',
    'white queen (0, 0)', 'white queen (0, 1)', 'white queen (0, 2)', 'white queen (0, 3)', 'white queen (0, 4)', 'white queen (0, 5)', 'white queen (0, 6)', 'white queen (0, 7)', 
    'white queen (1, 0)', 'white queen (1, 1)', 'white queen (1, 2)', 'white queen (1, 3)', 'white queen (1, 4)', 'white queen (1, 5)', 'white queen (1, 6)', 'white queen (1, 7)', 
    'white queen (2, 0)', 'white queen (2, 1)', 'white queen (2, 2)', 'white queen (2, 3)', 'white queen (2, 4)', 'white queen (2, 5)', 'white queen (2, 6)', 'white queen (2, 7)', 
    'white queen (3, 0)', 'white queen (3, 1)', 'white queen (3, 2)', 'white queen (3, 3)', 'white queen (3, 4)', 'white queen (3, 5)', 'white queen (3, 6)', 'white queen (3, 7)', 
    'white queen (4, 0)', 'white queen (4, 1)', 'white queen (4, 2)', 'white queen (4, 3)', 'white queen (4, 4)', 'white queen (4, 5)', 'white queen (4, 6)', 'white queen (4, 7)', 
    'white queen (5, 0)', 'white queen (5, 1)', 'white queen (5, 2)', 'white queen (5, 3)', 'white queen (5, 4)', 'white queen (5, 5)', 'white queen (5, 6)', 'white queen (5, 7)', 
    'white queen (6, 0)', 'white queen (6, 1)', 'white queen (6, 2)', 'white queen (6, 3)', 'white queen (6, 4)', 'white queen (6, 5)', 'white queen (6, 6)', 'white queen (6, 7)', 
    'white queen (7, 0)', 'white queen (7, 1)', 'white queen (7, 2)', 'white queen (7, 3)', 'white queen (7, 4)', 'white queen (7, 5)', 'white queen (7, 6)', 'white queen (7, 7)',
    'white pawn (0, 0)', 'white pawn (0, 1)', 'white pawn (0, 2)', 'white pawn (0, 3)', 'white pawn (0, 4)', 'white pawn (0, 5)', 'white pawn (0, 6)', 'white pawn (0, 7)', 
    'white pawn (1, 0)', 'white pawn (1, 1)', 'white pawn (1, 2)', 'white pawn (1, 3)', 'white pawn (1, 4)', 'white pawn (1, 5)', 'white pawn (1, 6)', 'white pawn (1, 7)', 
    'white pawn (2, 0)', 'white pawn (2, 1)', 'white pawn (2, 2)', 'white pawn (2, 3)', 'white pawn (2, 4)', 'white pawn (2, 5)', 'white pawn (2, 6)', 'white pawn (2, 7)', 
    'white pawn (3, 0)', 'white pawn (3, 1)', 'white pawn (3, 2)', 'white pawn (3, 3)', 'white pawn (3, 4)', 'white pawn (3, 5)', 'white pawn (3, 6)', 'white pawn (3, 7)', 
    'white pawn (4, 0)', 'white pawn (4, 1)', 'white pawn (4, 2)', 'white pawn (4, 3)', 'white pawn (4, 4)', 'white pawn (4, 5)', 'white pawn (4, 6)', 'white pawn (4, 7)', 
    'white pawn (5, 0)', 'white pawn (5, 1)', 'white pawn (5, 2)', 'white pawn (5, 3)', 'white pawn (5, 4)', 'white pawn (5, 5)', 'white pawn (5, 6)', 'white pawn (5, 7)', 
    'white pawn (6, 0)', 'white pawn (6, 1)', 'white pawn (6, 2)', 'white pawn (6, 3)', 'white pawn (6, 4)', 'white pawn (6, 5)', 'white pawn (6, 6)', 'white pawn (6, 7)', 
    'white pawn (7, 0)', 'white pawn (7, 1)', 'white pawn (7, 2)', 'white pawn (7, 3)', 'white pawn (7, 4)', 'white pawn (7, 5)', 'white pawn (7, 6)', 'white pawn (7, 7)']

all_black = ['black rook (0, 0)', 'black rook (0, 1)', 'black rook (0, 2)', 'black rook (0, 3)', 'black rook (0, 4)', 'black rook (0, 5)', 'black rook (0, 6)', 'black rook (0, 7)', 
    'black rook (1, 0)', 'black rook (1, 1)', 'black rook (1, 2)', 'black rook (1, 3)', 'black rook (1, 4)', 'black rook (1, 5)', 'black rook (1, 6)', 'black rook (1, 7)', 
    'black rook (2, 0)', 'black rook (2, 1)', 'black rook (2, 2)', 'black rook (2, 3)', 'black rook (2, 4)', 'black rook (2, 5)', 'black rook (2, 6)', 'black rook (2, 7)', 
    'black rook (3, 0)', 'black rook (3, 1)', 'black rook (3, 2)', 'black rook (3, 3)', 'black rook (3, 4)', 'black rook (3, 5)', 'black rook (3, 6)', 'black rook (3, 7)', 
    'black rook (4, 0)', 'black rook (4, 1)', 'black rook (4, 2)', 'black rook (4, 3)', 'black rook (4, 4)', 'black rook (4, 5)', 'black rook (4, 6)', 'black rook (4, 7)', 
    'black rook (5, 0)', 'black rook (5, 1)', 'black rook (5, 2)', 'black rook (5, 3)', 'black rook (5, 4)', 'black rook (5, 5)', 'black rook (5, 6)', 'black rook (5, 7)', 
    'black rook (6, 0)', 'black rook (6, 1)', 'black rook (6, 2)', 'black rook (6, 3)', 'black rook (6, 4)', 'black rook (6, 5)', 'black rook (6, 6)', 'black rook (6, 7)', 
    'black rook (7, 0)', 'black rook (7, 1)', 'black rook (7, 2)', 'black rook (7, 3)', 'black rook (7, 4)', 'black rook (7, 5)', 'black rook (7, 6)', 'black rook (7, 7)',
    'black knight (0, 0)', 'black knight (0, 1)', 'black knight (0, 2)', 'black knight (0, 3)', 'black knight (0, 4)', 'black knight (0, 5)', 'black knight (0, 6)', 'black knight (0, 7)', 
    'black knight (1, 0)', 'black knight (1, 1)', 'black knight (1, 2)', 'black knight (1, 3)', 'black knight (1, 4)', 'black knight (1, 5)', 'black knight (1, 6)', 'black knight (1, 7)', 
    'black knight (2, 0)', 'black knight (2, 1)', 'black knight (2, 2)', 'black knight (2, 3)', 'black knight (2, 4)', 'black knight (2, 5)', 'black knight (2, 6)', 'black knight (2, 7)', 
    'black knight (3, 0)', 'black knight (3, 1)', 'black knight (3, 2)', 'black knight (3, 3)', 'black knight (3, 4)', 'black knight (3, 5)', 'black knight (3, 6)', 'black knight (3, 7)', 
    'black knight (4, 0)', 'black knight (4, 1)', 'black knight (4, 2)', 'black knight (4, 3)', 'black knight (4, 4)', 'black knight (4, 5)', 'black knight (4, 6)', 'black knight (4, 7)', 
    'black knight (5, 0)', 'black knight (5, 1)', 'black knight (5, 2)', 'black knight (5, 3)', 'black knight (5, 4)', 'black knight (5, 5)', 'black knight (5, 6)', 'black knight (5, 7)', 
    'black knight (6, 0)', 'black knight (6, 1)', 'black knight (6, 2)', 'black knight (6, 3)', 'black knight (6, 4)', 'black knight (6, 5)', 'black knight (6, 6)', 'black knight (6, 7)', 
    'black knight (7, 0)', 'black knight (7, 1)', 'black knight (7, 2)', 'black knight (7, 3)', 'black knight (7, 4)', 'black knight (7, 5)', 'black knight (7, 6)', 'black knight (7, 7)',
    'black bishop (0, 0)', 'black bishop (0, 1)', 'black bishop (0, 2)', 'black bishop (0, 3)', 'black bishop (0, 4)', 'black bishop (0, 5)', 'black bishop (0, 6)', 'black bishop (0, 7)', 
    'black bishop (1, 0)', 'black bishop (1, 1)', 'black bishop (1, 2)', 'black bishop (1, 3)', 'black bishop (1, 4)', 'black bishop (1, 5)', 'black bishop (1, 6)', 'black bishop (1, 7)', 
    'black bishop (2, 0)', 'black bishop (2, 1)', 'black bishop (2, 2)', 'black bishop (2, 3)', 'black bishop (2, 4)', 'black bishop (2, 5)', 'black bishop (2, 6)', 'black bishop (2, 7)', 
    'black bishop (3, 0)', 'black bishop (3, 1)', 'black bishop (3, 2)', 'black bishop (3, 3)', 'black bishop (3, 4)', 'black bishop (3, 5)', 'black bishop (3, 6)', 'black bishop (3, 7)', 
    'black bishop (4, 0)', 'black bishop (4, 1)', 'black bishop (4, 2)', 'black bishop (4, 3)', 'black bishop (4, 4)', 'black bishop (4, 5)', 'black bishop (4, 6)', 'black bishop (4, 7)', 
    'black bishop (5, 0)', 'black bishop (5, 1)', 'black bishop (5, 2)', 'black bishop (5, 3)', 'black bishop (5, 4)', 'black bishop (5, 5)', 'black bishop (5, 6)', 'black bishop (5, 7)', 
    'black bishop (6, 0)', 'black bishop (6, 1)', 'black bishop (6, 2)', 'black bishop (6, 3)', 'black bishop (6, 4)', 'black bishop (6, 5)', 'black bishop (6, 6)', 'black bishop (6, 7)', 
    'black bishop (7, 0)', 'black bishop (7, 1)', 'black bishop (7, 2)', 'black bishop (7, 3)', 'black bishop (7, 4)', 'black bishop (7, 5)', 'black bishop (7, 6)', 'black bishop (7, 7)',
    'black king (0, 0)', 'black king (0, 1)', 'black king (0, 2)', 'black king (0, 3)', 'black king (0, 4)', 'black king (0, 5)', 'black king (0, 6)', 'black king (0, 7)', 
    'black king (1, 0)', 'black king (1, 1)', 'black king (1, 2)', 'black king (1, 3)', 'black king (1, 4)', 'black king (1, 5)', 'black king (1, 6)', 'black king (1, 7)', 
    'black king (2, 0)', 'black king (2, 1)', 'black king (2, 2)', 'black king (2, 3)', 'black king (2, 4)', 'black king (2, 5)', 'black king (2, 6)', 'black king (2, 7)', 
    'black king (3, 0)', 'black king (3, 1)', 'black king (3, 2)', 'black king (3, 3)', 'black king (3, 4)', 'black king (3, 5)', 'black king (3, 6)', 'black king (3, 7)', 
    'black king (4, 0)', 'black king (4, 1)', 'black king (4, 2)', 'black king (4, 3)', 'black king (4, 4)', 'black king (4, 5)', 'black king (4, 6)', 'black king (4, 7)', 
    'black king (5, 0)', 'black king (5, 1)', 'black king (5, 2)', 'black king (5, 3)', 'black king (5, 4)', 'black king (5, 5)', 'black king (5, 6)', 'black king (5, 7)', 
    'black king (6, 0)', 'black king (6, 1)', 'black king (6, 2)', 'black king (6, 3)', 'black king (6, 4)', 'black king (6, 5)', 'black king (6, 6)', 'black king (6, 7)', 
    'black king (7, 0)', 'black king (7, 1)', 'black king (7, 2)', 'black king (7, 3)', 'black king (7, 4)', 'black king (7, 5)', 'black king (7, 6)', 'black king (7, 7)',
    'black queen (0, 0)', 'black queen (0, 1)', 'black queen (0, 2)', 'black queen (0, 3)', 'black queen (0, 4)', 'black queen (0, 5)', 'black queen (0, 6)', 'black queen (0, 7)', 
    'black queen (1, 0)', 'black queen (1, 1)', 'black queen (1, 2)', 'black queen (1, 3)', 'black queen (1, 4)', 'black queen (1, 5)', 'black queen (1, 6)', 'black queen (1, 7)', 
    'black queen (2, 0)', 'black queen (2, 1)', 'black queen (2, 2)', 'black queen (2, 3)', 'black queen (2, 4)', 'black queen (2, 5)', 'black queen (2, 6)', 'black queen (2, 7)', 
    'black queen (3, 0)', 'black queen (3, 1)', 'black queen (3, 2)', 'black queen (3, 3)', 'black queen (3, 4)', 'black queen (3, 5)', 'black queen (3, 6)', 'black queen (3, 7)', 
    'black queen (4, 0)', 'black queen (4, 1)', 'black queen (4, 2)', 'black queen (4, 3)', 'black queen (4, 4)', 'black queen (4, 5)', 'black queen (4, 6)', 'black queen (4, 7)', 
    'black queen (5, 0)', 'black queen (5, 1)', 'black queen (5, 2)', 'black queen (5, 3)', 'black queen (5, 4)', 'black queen (5, 5)', 'black queen (5, 6)', 'black queen (5, 7)', 
    'black queen (6, 0)', 'black queen (6, 1)', 'black queen (6, 2)', 'black queen (6, 3)', 'black queen (6, 4)', 'black queen (6, 5)', 'black queen (6, 6)', 'black queen (6, 7)', 
    'black queen (7, 0)', 'black queen (7, 1)', 'black queen (7, 2)', 'black queen (7, 3)', 'black queen (7, 4)', 'black queen (7, 5)', 'black queen (7, 6)', 'black queen (7, 7)',
    'black pawn (0, 0)', 'black pawn (0, 1)', 'black pawn (0, 2)', 'black pawn (0, 3)', 'black pawn (0, 4)', 'black pawn (0, 5)', 'black pawn (0, 6)', 'black pawn (0, 7)', 
    'black pawn (1, 0)', 'black pawn (1, 1)', 'black pawn (1, 2)', 'black pawn (1, 3)', 'black pawn (1, 4)', 'black pawn (1, 5)', 'black pawn (1, 6)', 'black pawn (1, 7)', 
    'black pawn (2, 0)', 'black pawn (2, 1)', 'black pawn (2, 2)', 'black pawn (2, 3)', 'black pawn (2, 4)', 'black pawn (2, 5)', 'black pawn (2, 6)', 'black pawn (2, 7)', 
    'black pawn (3, 0)', 'black pawn (3, 1)', 'black pawn (3, 2)', 'black pawn (3, 3)', 'black pawn (3, 4)', 'black pawn (3, 5)', 'black pawn (3, 6)', 'black pawn (3, 7)', 
    'black pawn (4, 0)', 'black pawn (4, 1)', 'black pawn (4, 2)', 'black pawn (4, 3)', 'black pawn (4, 4)', 'black pawn (4, 5)', 'black pawn (4, 6)', 'black pawn (4, 7)', 
    'black pawn (5, 0)', 'black pawn (5, 1)', 'black pawn (5, 2)', 'black pawn (5, 3)', 'black pawn (5, 4)', 'black pawn (5, 5)', 'black pawn (5, 6)', 'black pawn (5, 7)', 
    'black pawn (6, 0)', 'black pawn (6, 1)', 'black pawn (6, 2)', 'black pawn (6, 3)', 'black pawn (6, 4)', 'black pawn (6, 5)', 'black pawn (6, 6)', 'black pawn (6, 7)', 
    'black pawn (7, 0)', 'black pawn (7, 1)', 'black pawn (7, 2)', 'black pawn (7, 3)', 'black pawn (7, 4)', 'black pawn (7, 5)', 'black pawn (7, 6)', 'black pawn (7, 7)']

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
# white pawn
white_knight = pygame.transform.scale(pygame.image.load('assets/images/white/knight.png'), (80, 80))
white_knight_small = pygame.transform.scale(white_knight, (45, 45))

# pawns ##########
# black pawn
black_pawn = pygame.transform.scale(pygame.image.load('assets/images/black/pawn.png'), (65, 65))
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))
# white pawn
white_pawn = pygame.transform.scale(pygame.image.load('assets/images/white/pawn.png'), (65, 65))
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))

# text backgrounds
white_text_bg = pygame.transform.scale(pygame.image.load('assets/images/white/move-text-bg.png'), (300, 45))
black_text_bg = pygame.transform.scale(pygame.image.load('assets/images/black/move-text-bg.png'), (300, 45))

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
moves_made_counter = 0
moves_made_list = []
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
left_click = ""
check = False