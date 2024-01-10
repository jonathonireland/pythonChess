from constants import *

def friendly_list(color):
    friends_list = []
    match color:
        case 'white':
            friends_list = white_locations    
        case 'black':
            friends_list = black_locations
    return friends_list

def enemy_list(color):
    enemies_list = []
    match color:
        case 'white':
            enemies_list = black_locations
        case 'black':
            enemies_list = white_locations
    return enemies_list

def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)
        
def draw_game_over(winner):
    pygame.draw.rect(screen, 'black', [200, 200, 400, 100])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

def pop_piece_out_lists(piece, color):
    if color == 'white':
        white_pieces.pop(piece)
        white_locations.pop(piece)
        white_moved.pop(piece)
    if color == 'black':
        black_pieces.pop(piece)
        black_locations.pop(piece)
        black_moved.pop(piece)
        
def write_moves_made(moves_made_list, color, moves_made_counter, column_two_counter, column_three_counter, column_four_counter):
    white_font_color = (255, 255, 255)
    black_font_color = (0, 0, 0)
    iteration_spacer = 1
    increment_pixels = 24
    if moves_made_counter == 1 or moves_made_counter > 1 and moves_made_counter < 33:
        iteration_spacer = moves_made_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1010, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1010, iteration_spacer))
    if moves_made_counter == 33 or moves_made_counter > 33 and moves_made_counter < 65:
        iteration_spacer = column_two_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1105, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1105, iteration_spacer))
    if moves_made_counter == 65 or moves_made_counter > 65 and moves_made_counter < 97:
        iteration_spacer = column_three_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1200, iteration_spacer))
        else:
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1200, iteration_spacer))
    if moves_made_counter == 97 or moves_made_counter > 97 and moves_made_counter < 129:
        iteration_spacer = column_four_counter * increment_pixels
        if color == 'white':
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, white_font_color), (1300, iteration_spacer))
        else: 
            screen.blit(small_font.render(str(moves_made_counter) + '. ' + all_moves[moves_made_list[-1]], True, black_font_color), (1300, iteration_spacer))
    print(str(moves_made_counter)+'. '+all_moves[moves_made_list[-1]])
        
