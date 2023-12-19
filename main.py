# two player chess in python with Pygame!
# part one, set up variables images and game loop
from typing import List, Tuple, Any

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
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
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
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))


def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red',
                                 [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1, 100, 100], 2)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue',
                                 [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1, 100, 100], 2)


# function to check all pieces valid options on board
def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        match piece:
            case 'pawn':
                moves_list = check_pawn(location, turn)
            case 'rook':
                moves_list = check_rook(location, turn)
            case 'knight':
                moves_list = check_knight(location, turn)
            case 'bishop':
                moves_list = check_bishop(location, turn)
            case 'queen':
                moves_list = check_queen(location, turn)
            case 'king':
                moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# check for valid moves for just selected piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    print(options_list)
    # valid_options = options_list[selection]
    if selection <= len(options_list):
        valid_options = options_list[selection]
        # return valid_options
    else:
        print('selection outside of options range!')
        valid_options = []

    return valid_options


def draw_valid(moves):
    # print(moves)
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# piece checks
# check if pawn can move
def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    elif color == 'black':
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list


def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    elif color == 'black':
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        match i:
            case 0:
                x = 0
                y = 1
            case 1:
                x = 0
                y = -1
            case 2:
                x = 1
                y = 0
            case 3:
                x = -1
                y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


def check_knight(position, color):
    pass


def check_bishop(position, color):
    pass


def check_queen(position, color):
    pass


def check_king(position, color):
    pass


black_options = check_options(black_pieces, black_locations, 'black')

white_options = check_options(white_pieces, white_locations, 'white')

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        print(selection)
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in white_locations:
                    selection = white_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    white_locations[selection] = click_coords
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in black_locations:
                    selection = black_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    black_locations[selection] = click_coords
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
    pygame.display.flip()
pygame.quit()
