from constants import *


# LISTING SERVICE FUNCTIONS #
def get_friendly_list(color): # Determine which Locations are Friendlies
    friends_list = []
    match color:
        case 'white':
            friends_list = white_locations    
        case 'black':
            friends_list = black_locations
    return friends_list


def get_enemy_list(color): # Determine which Locations are Enemies
    enemies_list = []
    match color:
        case 'white':
            enemies_list = black_locations
        case 'black':
            enemies_list = white_locations
    return enemies_list


# DRAWING SERVICE FUNCTIONS #
def draw_board(): # Draw Main Game Board
    screen.fill('white', (0, 0, (screen.get_width()//3)*1.85, BOARD_HEIGHT))
    screen.fill('dark gray', (BOARD_HEIGHT, 0, 2*SPACE_SIZE, BOARD_HEIGHT))
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [6*SPACE_SIZE - (column * (2*SPACE_SIZE)), row * SPACE_SIZE, SPACE_SIZE, SPACE_SIZE])
        else:
            pygame.draw.rect(screen, 'light gray', [7*SPACE_SIZE - (column * (2*SPACE_SIZE)), row * SPACE_SIZE, SPACE_SIZE, SPACE_SIZE])
        pygame.draw.rect(screen, 'gray', [0, BOARD_HEIGHT, WIDTH, SPACE_SIZE])
        pygame.draw.rect(screen, 'gold', [0, BOARD_HEIGHT, WIDTH, SPACE_SIZE], 5)
        pygame.draw.rect(screen, 'gold', [BOARD_HEIGHT, 0, 2*SPACE_SIZE, HEIGHT], 5)
        pygame.draw.rect(screen, 'black', [10*SPACE_SIZE, 0, 4*SPACE_SIZE, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, BOARD_HEIGHT+20))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, SPACE_SIZE * i), (BOARD_HEIGHT, SPACE_SIZE * i), 2)
            pygame.draw.line(screen, 'black', (SPACE_SIZE * i, 0), (SPACE_SIZE * i, BOARD_HEIGHT), 2)
        screen.blit(medium_font.render('FORFEIT', True, 'black'), (BOARD_HEIGHT + 10, BOARD_HEIGHT+30))
        if white_promote or black_promote:
            pygame.draw.rect(screen, 'gray', [0, BOARD_HEIGHT, WIDTH - 2*SPACE_SIZE, SPACE_SIZE])
            pygame.draw.rect(screen, 'gold', [0, BOARD_HEIGHT, WIDTH - 2*SPACE_SIZE, SPACE_SIZE], 5)
            screen.blit(big_font.render('Select Piece to Promote Pawn', True, 'black'), (20, BOARD_HEIGHT+20))

        
def draw_game_over(winner): # Draw Game Over Box and Text #
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


def draw_valid(moves): # Draw valid moves in game 
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * SPACE_SIZE + 50, moves[i][1] * SPACE_SIZE + 50), 5)


def draw_promotion(white_promote, black_promote): # Draw Pawn Promotion 
    pygame.draw.rect(screen, 'dark gray', [800, 0, 200, 420])
    color = ''
    if white_promote:
        color = 'white'
        for i in range(len(white_promotions)):
            piece = white_promotions[i]
            index = piece_list.index(piece)
            screen.blit(white_images[index], (BOARD_SIZE+60, 5 + SPACE_SIZE * i))
    if black_promote: 
        color = 'black'
        for i in range(len(black_promotions)):
            piece = black_promotions[i]
            index = piece_list.index(piece)
            screen.blit(black_images[index], (BOARD_SIZE+60, 5 + SPACE_SIZE * i))
    pygame.draw.rect(screen, color, [800, 0, 200, 420], 8)


def draw_castling(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0][0] * SPACE_SIZE + 50, moves[i][0][1] * SPACE_SIZE + 70), 8)
        screen.blit(font.render('king', True, 'black'), (moves[i][0][0] * 100 + 30, moves[i][0][1] * SPACE_SIZE + 70))
        pygame.draw.circle(screen, color, (moves[i][1][0] * SPACE_SIZE + 50, moves[i][1][1] * SPACE_SIZE + 70), 8)
        screen.blit(font.render('rook', True, 'black'),
                    (moves[i][1][0] * SPACE_SIZE + 30, moves[i][1][1] * SPACE_SIZE + 70))
        pygame.draw.line(screen, color, (moves[i][0][0] * SPACE_SIZE + 50, moves[i][0][1] * SPACE_SIZE + 70),
                         (moves[i][1][0] * SPACE_SIZE + 50, moves[i][1][1] * SPACE_SIZE + 70), 2)

def draw_previous_games():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])


def draw_moves_made(moves_made_list, color, moves_made_counter, column_two_counter, column_three_counter, column_four_counter): # Draw List of Moves as Game is Played
    white_font_color = (255, 255, 255)
    black_font_color = (0, 0, 0)
    iteration_spacer = 1
    increment_pixels = 24
    
    if moves_made_counter == 1 or moves_made_counter > 1 \
        and moves_made_counter < 33:
        iteration_spacer = moves_made_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1010, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1010, iteration_spacer))
    if moves_made_counter == 33 or moves_made_counter > 33 \
        and moves_made_counter < 65:
        iteration_spacer = column_two_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1105, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1105, iteration_spacer))
    if moves_made_counter == 65 or moves_made_counter > 65 \
        and moves_made_counter < 97:
        iteration_spacer = column_three_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1200, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1200, iteration_spacer))
    if moves_made_counter == 97 or moves_made_counter > 97 \
        and moves_made_counter < 129:
        iteration_spacer = column_four_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1300, iteration_spacer))
        else: 
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1300, iteration_spacer))
        
