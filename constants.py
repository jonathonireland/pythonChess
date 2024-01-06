import pygame
pygame.init()

WIDTH = 1300
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Two-Player Pygame Chess!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
small_font = pygame.font.Font('freesansbold.ttf', 12)
pygame.font.init()

timer = pygame.time.Clock()
fps = 60

# game variables and images
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
white_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
black_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
captured_pieces_white = []
captured_pieces_black = []

all_moves = ['player 1 moved white rook (0, 0)', 'player 1 moved white rook (0, 1)', 'player 1 moved white rook (0, 2)', 'player 1 moved white rook (0, 3)', 'player 1 moved white rook (0, 4)', 'player 1 moved white rook (0, 5)', 'player 1 moved white rook (0, 6)', 'player 1 moved white rook (0, 7)', 
    'player 1 moved white rook (1, 0)', 'player 1 moved white rook (1, 1)', 'player 1 moved white rook (1, 2)', 'player 1 moved white rook (1, 3)', 'player 1 moved white rook (1, 4)', 'player 1 moved white rook (1, 5)', 'player 1 moved white rook (1, 6)', 'player 1 moved white rook (1, 7)', 
    'player 1 moved white rook (2, 0)', 'player 1 moved white rook (2, 1)', 'player 1 moved white rook (2, 2)', 'player 1 moved white rook (2, 3)', 'player 1 moved white rook (2, 4)', 'player 1 moved white rook (2, 5)', 'player 1 moved white rook (2, 6)', 'player 1 moved white rook (2, 7)', 
    'player 1 moved white rook (3, 0)', 'player 1 moved white rook (3, 1)', 'player 1 moved white rook (3, 2)', 'player 1 moved white rook (3, 3)', 'player 1 moved white rook (3, 4)', 'player 1 moved white rook (3, 5)', 'player 1 moved white rook (3, 6)', 'player 1 moved white rook (3, 7)', 
    'player 1 moved white rook (4, 0)', 'player 1 moved white rook (4, 1)', 'player 1 moved white rook (4, 2)', 'player 1 moved white rook (4, 3)', 'player 1 moved white rook (4, 4)', 'player 1 moved white rook (4, 5)', 'player 1 moved white rook (4, 6)', 'player 1 moved white rook (4, 7)', 
    'player 1 moved white rook (5, 0)', 'player 1 moved white rook (5, 1)', 'player 1 moved white rook (5, 2)', 'player 1 moved white rook (5, 3)', 'player 1 moved white rook (5, 4)', 'player 1 moved white rook (5, 5)', 'player 1 moved white rook (5, 6)', 'player 1 moved white rook (5, 7)', 
    'player 1 moved white rook (6, 0)', 'player 1 moved white rook (6, 1)', 'player 1 moved white rook (6, 2)', 'player 1 moved white rook (6, 3)', 'player 1 moved white rook (6, 4)', 'player 1 moved white rook (6, 5)', 'player 1 moved white rook (6, 6)', 'player 1 moved white rook (6, 7)', 
    'player 1 moved white rook (7, 0)', 'player 1 moved white rook (7, 1)', 'player 1 moved white rook (7, 2)', 'player 1 moved white rook (7, 3)', 'player 1 moved white rook (7, 4)', 'player 1 moved white rook (7, 5)', 'player 1 moved white rook (7, 6)', 'player 1 moved white rook (7, 7)',
    'player 1 moved white knight (0, 0)', 'player 1 moved white knight (0, 1)', 'player 1 moved white knight (0, 2)', 'player 1 moved white knight (0, 3)', 'player 1 moved white knight (0, 4)', 'player 1 moved white knight (0, 5)', 'player 1 moved white knight (0, 6)', 'player 1 moved white knight (0, 7)', 
    'player 1 moved white knight (1, 0)', 'player 1 moved white knight (1, 1)', 'player 1 moved white knight (1, 2)', 'player 1 moved white knight (1, 3)', 'player 1 moved white knight (1, 4)', 'player 1 moved white knight (1, 5)', 'player 1 moved white knight (1, 6)', 'player 1 moved white knight (1, 7)', 
    'player 1 moved white knight (2, 0)', 'player 1 moved white knight (2, 1)', 'player 1 moved white knight (2, 2)', 'player 1 moved white knight (2, 3)', 'player 1 moved white knight (2, 4)', 'player 1 moved white knight (2, 5)', 'player 1 moved white knight (2, 6)', 'player 1 moved white knight (2, 7)', 
    'player 1 moved white knight (3, 0)', 'player 1 moved white knight (3, 1)', 'player 1 moved white knight (3, 2)', 'player 1 moved white knight (3, 3)', 'player 1 moved white knight (3, 4)', 'player 1 moved white knight (3, 5)', 'player 1 moved white knight (3, 6)', 'player 1 moved white knight (3, 7)', 
    'player 1 moved white knight (4, 0)', 'player 1 moved white knight (4, 1)', 'player 1 moved white knight (4, 2)', 'player 1 moved white knight (4, 3)', 'player 1 moved white knight (4, 4)', 'player 1 moved white knight (4, 5)', 'player 1 moved white knight (4, 6)', 'player 1 moved white knight (4, 7)', 
    'player 1 moved white knight (5, 0)', 'player 1 moved white knight (5, 1)', 'player 1 moved white knight (5, 2)', 'player 1 moved white knight (5, 3)', 'player 1 moved white knight (5, 4)', 'player 1 moved white knight (5, 5)', 'player 1 moved white knight (5, 6)', 'player 1 moved white knight (5, 7)', 
    'player 1 moved white knight (6, 0)', 'player 1 moved white knight (6, 1)', 'player 1 moved white knight (6, 2)', 'player 1 moved white knight (6, 3)', 'player 1 moved white knight (6, 4)', 'player 1 moved white knight (6, 5)', 'player 1 moved white knight (6, 6)', 'player 1 moved white knight (6, 7)', 
    'player 1 moved white knight (7, 0)', 'player 1 moved white knight (7, 1)', 'player 1 moved white knight (7, 2)', 'player 1 moved white knight (7, 3)', 'player 1 moved white knight (7, 4)', 'player 1 moved white knight (7, 5)', 'player 1 moved white knight (7, 6)', 'player 1 moved white knight (7, 7)',
    'player 1 moved white bishop (0, 0)', 'player 1 moved white bishop (0, 1)', 'player 1 moved white bishop (0, 2)', 'player 1 moved white bishop (0, 3)', 'player 1 moved white bishop (0, 4)', 'player 1 moved white bishop (0, 5)', 'player 1 moved white bishop (0, 6)', 'player 1 moved white bishop (0, 7)', 
    'player 1 moved white bishop (1, 0)', 'player 1 moved white bishop (1, 1)', 'player 1 moved white bishop (1, 2)', 'player 1 moved white bishop (1, 3)', 'player 1 moved white bishop (1, 4)', 'player 1 moved white bishop (1, 5)', 'player 1 moved white bishop (1, 6)', 'player 1 moved white bishop (1, 7)', 
    'player 1 moved white bishop (2, 0)', 'player 1 moved white bishop (2, 1)', 'player 1 moved white bishop (2, 2)', 'player 1 moved white bishop (2, 3)', 'player 1 moved white bishop (2, 4)', 'player 1 moved white bishop (2, 5)', 'player 1 moved white bishop (2, 6)', 'player 1 moved white bishop (2, 7)', 
    'player 1 moved white bishop (3, 0)', 'player 1 moved white bishop (3, 1)', 'player 1 moved white bishop (3, 2)', 'player 1 moved white bishop (3, 3)', 'player 1 moved white bishop (3, 4)', 'player 1 moved white bishop (3, 5)', 'player 1 moved white bishop (3, 6)', 'player 1 moved white bishop (3, 7)', 
    'player 1 moved white bishop (4, 0)', 'player 1 moved white bishop (4, 1)', 'player 1 moved white bishop (4, 2)', 'player 1 moved white bishop (4, 3)', 'player 1 moved white bishop (4, 4)', 'player 1 moved white bishop (4, 5)', 'player 1 moved white bishop (4, 6)', 'player 1 moved white bishop (4, 7)', 
    'player 1 moved white bishop (5, 0)', 'player 1 moved white bishop (5, 1)', 'player 1 moved white bishop (5, 2)', 'player 1 moved white bishop (5, 3)', 'player 1 moved white bishop (5, 4)', 'player 1 moved white bishop (5, 5)', 'player 1 moved white bishop (5, 6)', 'player 1 moved white bishop (5, 7)', 
    'player 1 moved white bishop (6, 0)', 'player 1 moved white bishop (6, 1)', 'player 1 moved white bishop (6, 2)', 'player 1 moved white bishop (6, 3)', 'player 1 moved white bishop (6, 4)', 'player 1 moved white bishop (6, 5)', 'player 1 moved white bishop (6, 6)', 'player 1 moved white bishop (6, 7)', 
    'player 1 moved white bishop (7, 0)', 'player 1 moved white bishop (7, 1)', 'player 1 moved white bishop (7, 2)', 'player 1 moved white bishop (7, 3)', 'player 1 moved white bishop (7, 4)', 'player 1 moved white bishop (7, 5)', 'player 1 moved white bishop (7, 6)', 'player 1 moved white bishop (7, 7)',
    'player 1 moved white king (0, 0)', 'player 1 moved white king (0, 1)', 'player 1 moved white king (0, 2)', 'player 1 moved white king (0, 3)', 'player 1 moved white king (0, 4)', 'player 1 moved white king (0, 5)', 'player 1 moved white king (0, 6)', 'player 1 moved white king (0, 7)', 
    'player 1 moved white king (1, 0)', 'player 1 moved white king (1, 1)', 'player 1 moved white king (1, 2)', 'player 1 moved white king (1, 3)', 'player 1 moved white king (1, 4)', 'player 1 moved white king (1, 5)', 'player 1 moved white king (1, 6)', 'player 1 moved white king (1, 7)', 
    'player 1 moved white king (2, 0)', 'player 1 moved white king (2, 1)', 'player 1 moved white king (2, 2)', 'player 1 moved white king (2, 3)', 'player 1 moved white king (2, 4)', 'player 1 moved white king (2, 5)', 'player 1 moved white king (2, 6)', 'player 1 moved white king (2, 7)', 
    'player 1 moved white king (3, 0)', 'player 1 moved white king (3, 1)', 'player 1 moved white king (3, 2)', 'player 1 moved white king (3, 3)', 'player 1 moved white king (3, 4)', 'player 1 moved white king (3, 5)', 'player 1 moved white king (3, 6)', 'player 1 moved white king (3, 7)', 
    'player 1 moved white king (4, 0)', 'player 1 moved white king (4, 1)', 'player 1 moved white king (4, 2)', 'player 1 moved white king (4, 3)', 'player 1 moved white king (4, 4)', 'player 1 moved white king (4, 5)', 'player 1 moved white king (4, 6)', 'player 1 moved white king (4, 7)', 
    'player 1 moved white king (5, 0)', 'player 1 moved white king (5, 1)', 'player 1 moved white king (5, 2)', 'player 1 moved white king (5, 3)', 'player 1 moved white king (5, 4)', 'player 1 moved white king (5, 5)', 'player 1 moved white king (5, 6)', 'player 1 moved white king (5, 7)', 
    'player 1 moved white king (6, 0)', 'player 1 moved white king (6, 1)', 'player 1 moved white king (6, 2)', 'player 1 moved white king (6, 3)', 'player 1 moved white king (6, 4)', 'player 1 moved white king (6, 5)', 'player 1 moved white king (6, 6)', 'player 1 moved white king (6, 7)', 
    'player 1 moved white king (7, 0)', 'player 1 moved white king (7, 1)', 'player 1 moved white king (7, 2)', 'player 1 moved white king (7, 3)', 'player 1 moved white king (7, 4)', 'player 1 moved white king (7, 5)', 'player 1 moved white king (7, 6)', 'player 1 moved white king (7, 7)',
    'player 1 moved white queen (0, 0)', 'player 1 moved white queen (0, 1)', 'player 1 moved white queen (0, 2)', 'player 1 moved white queen (0, 3)', 'player 1 moved white queen (0, 4)', 'player 1 moved white queen (0, 5)', 'player 1 moved white queen (0, 6)', 'player 1 moved white queen (0, 7)', 
    'player 1 moved white queen (1, 0)', 'player 1 moved white queen (1, 1)', 'player 1 moved white queen (1, 2)', 'player 1 moved white queen (1, 3)', 'player 1 moved white queen (1, 4)', 'player 1 moved white queen (1, 5)', 'player 1 moved white queen (1, 6)', 'player 1 moved white queen (1, 7)', 
    'player 1 moved white queen (2, 0)', 'player 1 moved white queen (2, 1)', 'player 1 moved white queen (2, 2)', 'player 1 moved white queen (2, 3)', 'player 1 moved white queen (2, 4)', 'player 1 moved white queen (2, 5)', 'player 1 moved white queen (2, 6)', 'player 1 moved white queen (2, 7)', 
    'player 1 moved white queen (3, 0)', 'player 1 moved white queen (3, 1)', 'player 1 moved white queen (3, 2)', 'player 1 moved white queen (3, 3)', 'player 1 moved white queen (3, 4)', 'player 1 moved white queen (3, 5)', 'player 1 moved white queen (3, 6)', 'player 1 moved white queen (3, 7)', 
    'player 1 moved white queen (4, 0)', 'player 1 moved white queen (4, 1)', 'player 1 moved white queen (4, 2)', 'player 1 moved white queen (4, 3)', 'player 1 moved white queen (4, 4)', 'player 1 moved white queen (4, 5)', 'player 1 moved white queen (4, 6)', 'player 1 moved white queen (4, 7)', 
    'player 1 moved white queen (5, 0)', 'player 1 moved white queen (5, 1)', 'player 1 moved white queen (5, 2)', 'player 1 moved white queen (5, 3)', 'player 1 moved white queen (5, 4)', 'player 1 moved white queen (5, 5)', 'player 1 moved white queen (5, 6)', 'player 1 moved white queen (5, 7)', 
    'player 1 moved white queen (6, 0)', 'player 1 moved white queen (6, 1)', 'player 1 moved white queen (6, 2)', 'player 1 moved white queen (6, 3)', 'player 1 moved white queen (6, 4)', 'player 1 moved white queen (6, 5)', 'player 1 moved white queen (6, 6)', 'player 1 moved white queen (6, 7)', 
    'player 1 moved white queen (7, 0)', 'player 1 moved white queen (7, 1)', 'player 1 moved white queen (7, 2)', 'player 1 moved white queen (7, 3)', 'player 1 moved white queen (7, 4)', 'player 1 moved white queen (7, 5)', 'player 1 moved white queen (7, 6)', 'player 1 moved white queen (7, 7)',
    'player 1 moved white pawn (0, 0)', 'player 1 moved white pawn (0, 1)', 'player 1 moved white pawn (0, 2)', 'player 1 moved white pawn (0, 3)', 'player 1 moved white pawn (0, 4)', 'player 1 moved white pawn (0, 5)', 'player 1 moved white pawn (0, 6)', 'player 1 moved white pawn (0, 7)', 
    'player 1 moved white pawn (1, 0)', 'player 1 moved white pawn (1, 1)', 'player 1 moved white pawn (1, 2)', 'player 1 moved white pawn (1, 3)', 'player 1 moved white pawn (1, 4)', 'player 1 moved white pawn (1, 5)', 'player 1 moved white pawn (1, 6)', 'player 1 moved white pawn (1, 7)', 
    'player 1 moved white pawn (2, 0)', 'player 1 moved white pawn (2, 1)', 'player 1 moved white pawn (2, 2)', 'player 1 moved white pawn (2, 3)', 'player 1 moved white pawn (2, 4)', 'player 1 moved white pawn (2, 5)', 'player 1 moved white pawn (2, 6)', 'player 1 moved white pawn (2, 7)', 
    'player 1 moved white pawn (3, 0)', 'player 1 moved white pawn (3, 1)', 'player 1 moved white pawn (3, 2)', 'player 1 moved white pawn (3, 3)', 'player 1 moved white pawn (3, 4)', 'player 1 moved white pawn (3, 5)', 'player 1 moved white pawn (3, 6)', 'player 1 moved white pawn (3, 7)', 
    'player 1 moved white pawn (4, 0)', 'player 1 moved white pawn (4, 1)', 'player 1 moved white pawn (4, 2)', 'player 1 moved white pawn (4, 3)', 'player 1 moved white pawn (4, 4)', 'player 1 moved white pawn (4, 5)', 'player 1 moved white pawn (4, 6)', 'player 1 moved white pawn (4, 7)', 
    'player 1 moved white pawn (5, 0)', 'player 1 moved white pawn (5, 1)', 'player 1 moved white pawn (5, 2)', 'player 1 moved white pawn (5, 3)', 'player 1 moved white pawn (5, 4)', 'player 1 moved white pawn (5, 5)', 'player 1 moved white pawn (5, 6)', 'player 1 moved white pawn (5, 7)', 
    'player 1 moved white pawn (6, 0)', 'player 1 moved white pawn (6, 1)', 'player 1 moved white pawn (6, 2)', 'player 1 moved white pawn (6, 3)', 'player 1 moved white pawn (6, 4)', 'player 1 moved white pawn (6, 5)', 'player 1 moved white pawn (6, 6)', 'player 1 moved white pawn (6, 7)', 
    'player 1 moved white pawn (7, 0)', 'player 1 moved white pawn (7, 1)', 'player 1 moved white pawn (7, 2)', 'player 1 moved white pawn (7, 3)', 'player 1 moved white pawn (7, 4)', 'player 1 moved white pawn (7, 5)', 'player 1 moved white pawn (7, 6)', 'player 1 moved white pawn (7, 7)',
    'player 2 moved black rook (0, 0)', 'player 2 moved black rook (0, 1)', 'player 2 moved black rook (0, 2)', 'player 2 moved black rook (0, 3)', 'player 2 moved black rook (0, 4)', 'player 2 moved black rook (0, 5)', 'player 2 moved black rook (0, 6)', 'player 2 moved black rook (0, 7)', 
    'player 2 moved black rook (1, 0)', 'player 2 moved black rook (1, 1)', 'player 2 moved black rook (1, 2)', 'player 2 moved black rook (1, 3)', 'player 2 moved black rook (1, 4)', 'player 2 moved black rook (1, 5)', 'player 2 moved black rook (1, 6)', 'player 2 moved black rook (1, 7)', 
    'player 2 moved black rook (2, 0)', 'player 2 moved black rook (2, 1)', 'player 2 moved black rook (2, 2)', 'player 2 moved black rook (2, 3)', 'player 2 moved black rook (2, 4)', 'player 2 moved black rook (2, 5)', 'player 2 moved black rook (2, 6)', 'player 2 moved black rook (2, 7)', 
    'player 2 moved black rook (3, 0)', 'player 2 moved black rook (3, 1)', 'player 2 moved black rook (3, 2)', 'player 2 moved black rook (3, 3)', 'player 2 moved black rook (3, 4)', 'player 2 moved black rook (3, 5)', 'player 2 moved black rook (3, 6)', 'player 2 moved black rook (3, 7)', 
    'player 2 moved black rook (4, 0)', 'player 2 moved black rook (4, 1)', 'player 2 moved black rook (4, 2)', 'player 2 moved black rook (4, 3)', 'player 2 moved black rook (4, 4)', 'player 2 moved black rook (4, 5)', 'player 2 moved black rook (4, 6)', 'player 2 moved black rook (4, 7)', 
    'player 2 moved black rook (5, 0)', 'player 2 moved black rook (5, 1)', 'player 2 moved black rook (5, 2)', 'player 2 moved black rook (5, 3)', 'player 2 moved black rook (5, 4)', 'player 2 moved black rook (5, 5)', 'player 2 moved black rook (5, 6)', 'player 2 moved black rook (5, 7)', 
    'player 2 moved black rook (6, 0)', 'player 2 moved black rook (6, 1)', 'player 2 moved black rook (6, 2)', 'player 2 moved black rook (6, 3)', 'player 2 moved black rook (6, 4)', 'player 2 moved black rook (6, 5)', 'player 2 moved black rook (6, 6)', 'player 2 moved black rook (6, 7)', 
    'player 2 moved black rook (7, 0)', 'player 2 moved black rook (7, 1)', 'player 2 moved black rook (7, 2)', 'player 2 moved black rook (7, 3)', 'player 2 moved black rook (7, 4)', 'player 2 moved black rook (7, 5)', 'player 2 moved black rook (7, 6)', 'player 2 moved black rook (7, 7)',
    'player 2 moved black knight (0, 0)', 'player 2 moved black knight (0, 1)', 'player 2 moved black knight (0, 2)', 'player 2 moved black knight (0, 3)', 'player 2 moved black knight (0, 4)', 'player 2 moved black knight (0, 5)', 'player 2 moved black knight (0, 6)', 'player 2 moved black knight (0, 7)', 
    'player 2 moved black knight (1, 0)', 'player 2 moved black knight (1, 1)', 'player 2 moved black knight (1, 2)', 'player 2 moved black knight (1, 3)', 'player 2 moved black knight (1, 4)', 'player 2 moved black knight (1, 5)', 'player 2 moved black knight (1, 6)', 'player 2 moved black knight (1, 7)', 
    'player 2 moved black knight (2, 0)', 'player 2 moved black knight (2, 1)', 'player 2 moved black knight (2, 2)', 'player 2 moved black knight (2, 3)', 'player 2 moved black knight (2, 4)', 'player 2 moved black knight (2, 5)', 'player 2 moved black knight (2, 6)', 'player 2 moved black knight (2, 7)', 
    'player 2 moved black knight (3, 0)', 'player 2 moved black knight (3, 1)', 'player 2 moved black knight (3, 2)', 'player 2 moved black knight (3, 3)', 'player 2 moved black knight (3, 4)', 'player 2 moved black knight (3, 5)', 'player 2 moved black knight (3, 6)', 'player 2 moved black knight (3, 7)', 
    'player 2 moved black knight (4, 0)', 'player 2 moved black knight (4, 1)', 'player 2 moved black knight (4, 2)', 'player 2 moved black knight (4, 3)', 'player 2 moved black knight (4, 4)', 'player 2 moved black knight (4, 5)', 'player 2 moved black knight (4, 6)', 'player 2 moved black knight (4, 7)', 
    'player 2 moved black knight (5, 0)', 'player 2 moved black knight (5, 1)', 'player 2 moved black knight (5, 2)', 'player 2 moved black knight (5, 3)', 'player 2 moved black knight (5, 4)', 'player 2 moved black knight (5, 5)', 'player 2 moved black knight (5, 6)', 'player 2 moved black knight (5, 7)', 
    'player 2 moved black knight (6, 0)', 'player 2 moved black knight (6, 1)', 'player 2 moved black knight (6, 2)', 'player 2 moved black knight (6, 3)', 'player 2 moved black knight (6, 4)', 'player 2 moved black knight (6, 5)', 'player 2 moved black knight (6, 6)', 'player 2 moved black knight (6, 7)', 
    'player 2 moved black knight (7, 0)', 'player 2 moved black knight (7, 1)', 'player 2 moved black knight (7, 2)', 'player 2 moved black knight (7, 3)', 'player 2 moved black knight (7, 4)', 'player 2 moved black knight (7, 5)', 'player 2 moved black knight (7, 6)', 'player 2 moved black knight (7, 7)',
    'player 2 moved black bishop (0, 0)', 'player 2 moved black bishop (0, 1)', 'player 2 moved black bishop (0, 2)', 'player 2 moved black bishop (0, 3)', 'player 2 moved black bishop (0, 4)', 'player 2 moved black bishop (0, 5)', 'player 2 moved black bishop (0, 6)', 'player 2 moved black bishop (0, 7)', 
    'player 2 moved black bishop (1, 0)', 'player 2 moved black bishop (1, 1)', 'player 2 moved black bishop (1, 2)', 'player 2 moved black bishop (1, 3)', 'player 2 moved black bishop (1, 4)', 'player 2 moved black bishop (1, 5)', 'player 2 moved black bishop (1, 6)', 'player 2 moved black bishop (1, 7)', 
    'player 2 moved black bishop (2, 0)', 'player 2 moved black bishop (2, 1)', 'player 2 moved black bishop (2, 2)', 'player 2 moved black bishop (2, 3)', 'player 2 moved black bishop (2, 4)', 'player 2 moved black bishop (2, 5)', 'player 2 moved black bishop (2, 6)', 'player 2 moved black bishop (2, 7)', 
    'player 2 moved black bishop (3, 0)', 'player 2 moved black bishop (3, 1)', 'player 2 moved black bishop (3, 2)', 'player 2 moved black bishop (3, 3)', 'player 2 moved black bishop (3, 4)', 'player 2 moved black bishop (3, 5)', 'player 2 moved black bishop (3, 6)', 'player 2 moved black bishop (3, 7)', 
    'player 2 moved black bishop (4, 0)', 'player 2 moved black bishop (4, 1)', 'player 2 moved black bishop (4, 2)', 'player 2 moved black bishop (4, 3)', 'player 2 moved black bishop (4, 4)', 'player 2 moved black bishop (4, 5)', 'player 2 moved black bishop (4, 6)', 'player 2 moved black bishop (4, 7)', 
    'player 2 moved black bishop (5, 0)', 'player 2 moved black bishop (5, 1)', 'player 2 moved black bishop (5, 2)', 'player 2 moved black bishop (5, 3)', 'player 2 moved black bishop (5, 4)', 'player 2 moved black bishop (5, 5)', 'player 2 moved black bishop (5, 6)', 'player 2 moved black bishop (5, 7)', 
    'player 2 moved black bishop (6, 0)', 'player 2 moved black bishop (6, 1)', 'player 2 moved black bishop (6, 2)', 'player 2 moved black bishop (6, 3)', 'player 2 moved black bishop (6, 4)', 'player 2 moved black bishop (6, 5)', 'player 2 moved black bishop (6, 6)', 'player 2 moved black bishop (6, 7)', 
    'player 2 moved black bishop (7, 0)', 'player 2 moved black bishop (7, 1)', 'player 2 moved black bishop (7, 2)', 'player 2 moved black bishop (7, 3)', 'player 2 moved black bishop (7, 4)', 'player 2 moved black bishop (7, 5)', 'player 2 moved black bishop (7, 6)', 'player 2 moved black bishop (7, 7)',
    'player 2 moved black king (0, 0)', 'player 2 moved black king (0, 1)', 'player 2 moved black king (0, 2)', 'player 2 moved black king (0, 3)', 'player 2 moved black king (0, 4)', 'player 2 moved black king (0, 5)', 'player 2 moved black king (0, 6)', 'player 2 moved black king (0, 7)', 
    'player 2 moved black king (1, 0)', 'player 2 moved black king (1, 1)', 'player 2 moved black king (1, 2)', 'player 2 moved black king (1, 3)', 'player 2 moved black king (1, 4)', 'player 2 moved black king (1, 5)', 'player 2 moved black king (1, 6)', 'player 2 moved black king (1, 7)', 
    'player 2 moved black king (2, 0)', 'player 2 moved black king (2, 1)', 'player 2 moved black king (2, 2)', 'player 2 moved black king (2, 3)', 'player 2 moved black king (2, 4)', 'player 2 moved black king (2, 5)', 'player 2 moved black king (2, 6)', 'player 2 moved black king (2, 7)', 
    'player 2 moved black king (3, 0)', 'player 2 moved black king (3, 1)', 'player 2 moved black king (3, 2)', 'player 2 moved black king (3, 3)', 'player 2 moved black king (3, 4)', 'player 2 moved black king (3, 5)', 'player 2 moved black king (3, 6)', 'player 2 moved black king (3, 7)', 
    'player 2 moved black king (4, 0)', 'player 2 moved black king (4, 1)', 'player 2 moved black king (4, 2)', 'player 2 moved black king (4, 3)', 'player 2 moved black king (4, 4)', 'player 2 moved black king (4, 5)', 'player 2 moved black king (4, 6)', 'player 2 moved black king (4, 7)', 
    'player 2 moved black king (5, 0)', 'player 2 moved black king (5, 1)', 'player 2 moved black king (5, 2)', 'player 2 moved black king (5, 3)', 'player 2 moved black king (5, 4)', 'player 2 moved black king (5, 5)', 'player 2 moved black king (5, 6)', 'player 2 moved black king (5, 7)', 
    'player 2 moved black king (6, 0)', 'player 2 moved black king (6, 1)', 'player 2 moved black king (6, 2)', 'player 2 moved black king (6, 3)', 'player 2 moved black king (6, 4)', 'player 2 moved black king (6, 5)', 'player 2 moved black king (6, 6)', 'player 2 moved black king (6, 7)', 
    'player 2 moved black king (7, 0)', 'player 2 moved black king (7, 1)', 'player 2 moved black king (7, 2)', 'player 2 moved black king (7, 3)', 'player 2 moved black king (7, 4)', 'player 2 moved black king (7, 5)', 'player 2 moved black king (7, 6)', 'player 2 moved black king (7, 7)',
    'player 2 moved black queen (0, 0)', 'player 2 moved black queen (0, 1)', 'player 2 moved black queen (0, 2)', 'player 2 moved black queen (0, 3)', 'player 2 moved black queen (0, 4)', 'player 2 moved black queen (0, 5)', 'player 2 moved black queen (0, 6)', 'player 2 moved black queen (0, 7)', 
    'player 2 moved black queen (1, 0)', 'player 2 moved black queen (1, 1)', 'player 2 moved black queen (1, 2)', 'player 2 moved black queen (1, 3)', 'player 2 moved black queen (1, 4)', 'player 2 moved black queen (1, 5)', 'player 2 moved black queen (1, 6)', 'player 2 moved black queen (1, 7)', 
    'player 2 moved black queen (2, 0)', 'player 2 moved black queen (2, 1)', 'player 2 moved black queen (2, 2)', 'player 2 moved black queen (2, 3)', 'player 2 moved black queen (2, 4)', 'player 2 moved black queen (2, 5)', 'player 2 moved black queen (2, 6)', 'player 2 moved black queen (2, 7)', 
    'player 2 moved black queen (3, 0)', 'player 2 moved black queen (3, 1)', 'player 2 moved black queen (3, 2)', 'player 2 moved black queen (3, 3)', 'player 2 moved black queen (3, 4)', 'player 2 moved black queen (3, 5)', 'player 2 moved black queen (3, 6)', 'player 2 moved black queen (3, 7)', 
    'player 2 moved black queen (4, 0)', 'player 2 moved black queen (4, 1)', 'player 2 moved black queen (4, 2)', 'player 2 moved black queen (4, 3)', 'player 2 moved black queen (4, 4)', 'player 2 moved black queen (4, 5)', 'player 2 moved black queen (4, 6)', 'player 2 moved black queen (4, 7)', 
    'player 2 moved black queen (5, 0)', 'player 2 moved black queen (5, 1)', 'player 2 moved black queen (5, 2)', 'player 2 moved black queen (5, 3)', 'player 2 moved black queen (5, 4)', 'player 2 moved black queen (5, 5)', 'player 2 moved black queen (5, 6)', 'player 2 moved black queen (5, 7)', 
    'player 2 moved black queen (6, 0)', 'player 2 moved black queen (6, 1)', 'player 2 moved black queen (6, 2)', 'player 2 moved black queen (6, 3)', 'player 2 moved black queen (6, 4)', 'player 2 moved black queen (6, 5)', 'player 2 moved black queen (6, 6)', 'player 2 moved black queen (6, 7)', 
    'player 2 moved black queen (7, 0)', 'player 2 moved black queen (7, 1)', 'player 2 moved black queen (7, 2)', 'player 2 moved black queen (7, 3)', 'player 2 moved black queen (7, 4)', 'player 2 moved black queen (7, 5)', 'player 2 moved black queen (7, 6)', 'player 2 moved black queen (7, 7)',
    'player 2 moved black pawn (0, 0)', 'player 2 moved black pawn (0, 1)', 'player 2 moved black pawn (0, 2)', 'player 2 moved black pawn (0, 3)', 'player 2 moved black pawn (0, 4)', 'player 2 moved black pawn (0, 5)', 'player 2 moved black pawn (0, 6)', 'player 2 moved black pawn (0, 7)', 
    'player 2 moved black pawn (1, 0)', 'player 2 moved black pawn (1, 1)', 'player 2 moved black pawn (1, 2)', 'player 2 moved black pawn (1, 3)', 'player 2 moved black pawn (1, 4)', 'player 2 moved black pawn (1, 5)', 'player 2 moved black pawn (1, 6)', 'player 2 moved black pawn (1, 7)', 
    'player 2 moved black pawn (2, 0)', 'player 2 moved black pawn (2, 1)', 'player 2 moved black pawn (2, 2)', 'player 2 moved black pawn (2, 3)', 'player 2 moved black pawn (2, 4)', 'player 2 moved black pawn (2, 5)', 'player 2 moved black pawn (2, 6)', 'player 2 moved black pawn (2, 7)', 
    'player 2 moved black pawn (3, 0)', 'player 2 moved black pawn (3, 1)', 'player 2 moved black pawn (3, 2)', 'player 2 moved black pawn (3, 3)', 'player 2 moved black pawn (3, 4)', 'player 2 moved black pawn (3, 5)', 'player 2 moved black pawn (3, 6)', 'player 2 moved black pawn (3, 7)', 
    'player 2 moved black pawn (4, 0)', 'player 2 moved black pawn (4, 1)', 'player 2 moved black pawn (4, 2)', 'player 2 moved black pawn (4, 3)', 'player 2 moved black pawn (4, 4)', 'player 2 moved black pawn (4, 5)', 'player 2 moved black pawn (4, 6)', 'player 2 moved black pawn (4, 7)', 
    'player 2 moved black pawn (5, 0)', 'player 2 moved black pawn (5, 1)', 'player 2 moved black pawn (5, 2)', 'player 2 moved black pawn (5, 3)', 'player 2 moved black pawn (5, 4)', 'player 2 moved black pawn (5, 5)', 'player 2 moved black pawn (5, 6)', 'player 2 moved black pawn (5, 7)', 
    'player 2 moved black pawn (6, 0)', 'player 2 moved black pawn (6, 1)', 'player 2 moved black pawn (6, 2)', 'player 2 moved black pawn (6, 3)', 'player 2 moved black pawn (6, 4)', 'player 2 moved black pawn (6, 5)', 'player 2 moved black pawn (6, 6)', 'player 2 moved black pawn (6, 7)', 
    'player 2 moved black pawn (7, 0)', 'player 2 moved black pawn (7, 1)', 'player 2 moved black pawn (7, 2)', 'player 2 moved black pawn (7, 3)', 'player 2 moved black pawn (7, 4)', 'player 2 moved black pawn (7, 5)', 'player 2 moved black pawn (7, 6)', 'player 2 moved black pawn (7, 7)']

turn_step = 0
# 0 - whites turn no selction: 1- whites turn piece selected: 2 - player 2 moved black turn no selection
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

# chess board numbers
chess_board_numbers = pygame.transform.scale(pygame.image.load('assets/images/chess-board-numbers.png'), (800, 800))

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
moves_made_list_box = ""
winner = ''
game_over = False
white_ep = (100, 100)
black_ep = (100, 100)
white_promote = False
black_promote = False
promo_index = 100
left_click = ""
check = False