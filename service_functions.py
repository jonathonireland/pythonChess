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

def pop_piece_out_lists(piece, color):
    if color == 'white':
        white_pieces.pop(piece)
        white_locations.pop(piece)
        white_moved.pop(piece)
    if color == 'black':
        black_pieces.pop(piece)
        black_locations.pop(piece)
        black_moved.pop(piece)
        
