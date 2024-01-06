from constants import *

import pygame

pygame.init()

# draw main game board
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
        pygame.draw.rect(screen, 'black', [1000, 0, 300, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (810, 830))
        if white_promote or black_promote:
            pygame.draw.rect(screen, 'gray', [0, 800, WIDTH - 200, 100])
            pygame.draw.rect(screen, 'gold', [0, 800, WIDTH - 200, 100], 5)
            screen.blit(big_font.render('Select Piece to Promote Pawn', True, 'black'), (20, 820))
    screen.blit(chess_board_numbers, (5,5))


# draw pieces onto board
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

                
# draw captured pieces
def draw_captured():
    for i in range(len(captured_pieces_white)):
        captured_piece = captured_pieces_white[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_black_images[index], (825, 5 + 50*i))
    for i in range(len(captured_pieces_black)):
        captured_piece = captured_pieces_black[i]
        index = piece_list.index(captured_piece)
        screen.blit(small_white_images[index], (925, 5 + 50*i))
          

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 50])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))
    

def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)
        
def draw_single_move(moves_made_counter, iteration_spacer, move_made, white_font_color):
    screen.blit(small_font.render(str(moves_made_counter) + '. ' + move_made, True, white_font_color), (1010, iteration_spacer))


