# import pygame
from constants import *
from db_functions import *
from service_functions import *
pygame.init()

def check_bishop(position, color): # Check Bishop's Valid Moves
    moves_list = []
    friends_list = friendly_list(color)
    enemies_list = enemy_list(color)  
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        match i:
            case 0:
                x = 1
                y = -1
            case 1:
                x = -1
                y = -1
            case 2:
                x = 1
                y = 1
            case 3:
                x = -1
                y = 1
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

def check_knight(position, color): # Check Knight's Valid Moves
    moves_list = []
    friends_list = friendly_list(color)
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_pawn(position, color): # Check if Pawn Can Move
    moves_list = []
    match color:
        case 'white':
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
            # add en passant move checker
            if (position[0] + 1, position[1] + 1) == black_ep:
                moves_list.append((position[0] + 1, position[1] + 1))
            if (position[0] - 1, position[1] + 1) == black_ep:
                moves_list.append((position[0] - 1, position[1] + 1))
        case 'black':
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
            # add en passant move checker
            if (position[0] + 1, position[1] - 1) == white_ep:
                moves_list.append((position[0] + 1, position[1] - 1))
            if (position[0] - 1, position[1] - 1) == white_ep:
                moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_queen(position, color): # Check Queen's Valid Moves
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_rook(position, color): # Check if Rook Can Move
    moves_list = []
    friends_list = friendly_list(color)
    enemies_list = enemy_list(color)  
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

def draw_check(): # Draw a Flashing Square Around King if in Check
    global check
    check = False
    if turn_step < 2:
        if 'king' in white_pieces:
            king_index = white_pieces.index('king')
            king_location = white_locations[king_index]
            for i in range(len(black_options)):
                if king_location in black_options[i]:
                    print(str(black_options[i]))
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in black_pieces:
            king_index = black_pieces.index('king')
            king_location = black_locations[king_index]
            for i in range(len(white_options)):
                if king_location in white_options[i]:
                    print(str(white_options[i]))
                    check = True
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)

def check_options(pieces, locations, turn): # Check All Pieces Valid Options on Board
    global castling_moves
    moves_list = []
    all_moves_list = []
    castling_moves = []
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
                moves_list, castling_moves = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_valid_moves(): # Check for Valid Moves for Selected Piece
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    if selection <= len(options_list):
        valid_options = options_list[selection]
    else:
        print('selection outside of options range!')
        valid_options = []
    return valid_options

def check_ep(old_coords, new_coords): # Check en passant 
    if turn_step <= 1:
        index = white_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] - 1)
        piece = white_pieces[index]
    else: 
        index = black_locations.index(old_coords)
        ep_coords = (new_coords[0], new_coords[1] + 1)
        piece = black_pieces[index]
    if piece == 'pawn' and abs(old_coords[1] - new_coords[1]) > 1:
        # if piece was pawn and moved two spaces, return EP coords as defined above
        pass
    else: 
        ep_coords = (100, 100)
    return ep_coords

def check_promotion(): # Check to Add Pawn Promotion
    pawn_indexes = []
    white_promotion = False
    black_promotion = False
    promote_index = 100
    for i in range(len(white_pieces)):
        if white_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if white_locations[pawn_indexes[i]][1] == 7:
            white_promotion = True
            promote_index = pawn_indexes[i]
    pawn_indexes = []
    for i in range(len(black_pieces)):
        if black_pieces[i] == 'pawn':
            pawn_indexes.append(i)
    for i in range(len(pawn_indexes)):
        if black_locations[pawn_indexes[i]][1] == 0:
            black_promotion = True
            promote_index = pawn_indexes[i]
    return white_promotion, black_promotion, promote_index

def check_castling(): # Check if Castling is Possible
    castle_moves = []  # store each valid castle move as [((king_coords), (castle_coords))]
    rook_indexes = []
    rook_locations = []
    king_index = 0
    king_pos = (0, 0)
    if turn_step > 1:
        for i in range(len(white_pieces)):
            if white_pieces[i] == 'rook':
                rook_indexes.append(white_moved[i])
                rook_locations.append(white_locations[i])
            if white_pieces[i] == 'king':
                king_index = i
                king_pos = white_locations[i]
        if not white_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in black_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    else:
        for i in range(len(black_pieces)):
            if black_pieces[i] == 'rook':
                rook_indexes.append(black_moved[i])
                rook_locations.append(black_locations[i])
            if black_pieces[i] == 'king':
                king_index = i
                king_pos = black_locations[i]
        if not black_moved[king_index] and False in rook_indexes and not check:
            for i in range(len(rook_indexes)):
                castle = True
                if rook_locations[i][0] > king_pos[0]:
                    empty_squares = [(king_pos[0] + 1, king_pos[1]), (king_pos[0] + 2, king_pos[1]),
                                     (king_pos[0] + 3, king_pos[1])]
                else:
                    empty_squares = [(king_pos[0] - 1, king_pos[1]), (king_pos[0] - 2, king_pos[1])]
                for j in range(len(empty_squares)):
                    if empty_squares[j] in white_locations or empty_squares[j] in black_locations or \
                            empty_squares[j] in white_options or rook_indexes[i]:
                        castle = False
                if castle:
                    castle_moves.append((empty_squares[1], empty_squares[0]))
    return castle_moves

def check_king(position, color): # Check King's Valid Moves
    moves_list = []
    castle_moves = check_castling()
    friends_list = friendly_list(color)
        # 8 squares to check for kings
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list, castle_moves
    
def check_promo_select(): # Check Promotion Options
    mouse_pos = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    x_pos = mouse_pos[0] // 100 
    y_pos = mouse_pos[1] // 100
    color = ''
    piece = ''
    promotion_id =''
    global moveid
    if white_promote and left_click and x_pos > 7 and y_pos < 4:
        white_pieces[promo_index] = white_promotions[y_pos]
        color = 'white'
        piece = white_pieces[promo_index]
        promotion_id = str(piece)+str(moveid)+str(color)
    if black_promote and left_click and x_pos > 7 and y_pos < 4:
        black_pieces[promo_index] = black_promotions[y_pos]
        color = 'black'
        piece = black_pieces[promo_index]
        promotion_id = str(piece)+str(moveid)+str(color)
    record_pawn_promotion(piece, moveid, color, promotion_id)
    
def draw_captured(): # Draw Captured Pieces 
    captured_piece = ''
    color = ''
    captured_id = ''
    if len(captured_pieces_white) > 0 or len(captured_pieces_black) > 0:
        for i in range(len(captured_pieces_white)):
            captured_piece = captured_pieces_white[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_black_images[index], (825, 5 + 50*i))
        for i in range(len(captured_pieces_black)):
            captured_piece = captured_pieces_black[i]
            index = piece_list.index(captured_piece)
            screen.blit(small_white_images[index], (925, 5 + 50*i))

def get_both_options(): # Get Options from check_options 
    black_options = check_options(black_pieces, black_locations, 'black')
    white_options = check_options(white_pieces, white_locations, 'white')
    return black_options, white_options

def create_new_game(): # Create a New Game in Persistant Data
    sql = "INSERT INTO games (game_name, game_notes) VALUES (%s, %s)"
    val = ("newGame", "initial attempt")
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        global gameid
        gameid = mycursor.lastrowid
        print(str(gameid) + " game id has a value")
    except:
        mydb.rollback()

def record_game_move(gameid, moves_made_counter, color, selected_piece, selection, click_coords):
    sql = "INSERT INTO gameMoves (games_id, order_number, color, piece, start_pos, end_pos) VALUES ('"+str(gameid)+"', '"+str(moves_made_counter)+"', '"+color+"', '"+str(selected_piece)+"', '"+str(selection)+"', '"+str(click_coords)+"')"
    try:
        mycursor.execute(sql)
        mydb.commit()
        global moveid
        moveid = mycursor.lastrowid
        print(str(moveid) + " move id has a value")
    except:
        mydb.rollback()

# Clean Start Game Variables and Begin While Run Loop
create_new_game()
black_options = get_both_options()[0]
white_options = get_both_options()[1]
column_two_counter = 0
column_three_counter = 0
column_four_counter = 0
run = True
screen.fill('dark gray')
while run:
    timer.tick(fps)
    screen.fill('white', (0, 0, (screen.get_width()//3)*1.85, screen.get_height()))
    screen.fill('dark gray', (800, 0, 200, HEIGHT))
    if counter < 30:
        counter += 1    
    else:
        counter = 0
    draw_board()
    draw_pieces()
    draw_check()
    draw_captured()
    if not game_over: 
        white_promote, black_promote, promo_index = check_promotion()
        if white_promote or black_promote:
            draw_promotion(white_promote, black_promote)
            check_promo_select()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
        if selected_piece == 'king':
            draw_castling(castling_moves)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            # white's turn
            if turn_step <= 1:
                
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black' # stops game play
                    
                if click_coords in white_locations:
                    # first click
                    selection = white_locations.index(click_coords)
                    
                    # check what piece is selected, so you can only draw castling if king is selected
                    selected_piece = white_pieces[selection]
                    
                    # second click
                    if turn_step == 0:
                        turn_step = 1
                        
                if click_coords in valid_moves and selection != 100:
                    white_ep = check_ep(white_locations[selection], click_coords)
                    
                    # record previous move to pass it to record game moves
                    previous_white_locations.append(white_locations[selection])
                    
                    # change white locations selected coords
                    white_locations[selection] = click_coords
                    
                    # change boolean for selection to True if it's False
                    if white_moved[selection] == False:
                        white_moved[selection] = True
                    
                    # increment moves made counter!! 
                    moves_made_counter += 1
                    
                    # column counter logic
                    if moves_made_counter == 33:
                        column_two_counter = 1
                    if moves_made_counter > 33 and moves_made_counter < 65:
                        column_two_counter += 1
                    if moves_made_counter == 65:
                        column_three_counter = 1
                    if moves_made_counter > 65 and moves_made_counter < 97:
                        column_three_counter += 1
                    if moves_made_counter == 97:
                        column_four_counter = 1
                    if moves_made_counter > 97 and moves_made_counter < 129:
                        column_four_counter += 1
                        
                    # log game move to gameMoves table
                    record_game_move(gameid,moves_made_counter,'white',selected_piece,previous_white_locations[-1],click_coords)
                    
                    # append to moves list
                    moves_made_list.append(all_moves.index(selected_piece +' '+ str(click_coords) ))
                    
                    # display moves to right column
                    draw_moves_made(moves_made_list, 'white', moves_made_counter, column_two_counter, column_three_counter, column_four_counter)
                    
                    # record capture of black piece
                    if click_coords in black_locations:
                        black_piece = black_locations.index(click_coords)
                        captured_pieces_white.append(black_pieces[black_piece])
                        color = 'white'
                        captured_id = str(black_pieces[black_piece])+str(moveid)+str(color)
                        record_captured_piece(black_pieces[black_piece], moveid, color, captured_id)
                        if black_pieces[black_piece] == 'king':
                            winner = 'white'
                        pop_piece_out_lists(black_piece, 'black')

                    # En passant logic    
                    if click_coords == black_ep:
                        black_piece = black_locations.index((black_ep[0], black_ep[1]-1))
                        captured_pieces_white.append(black_pieces[black_piece])
                        color = 'white'
                        captured_id = str(black_pieces[black_piece])+str(moveid)+str(color)
                        record_captured_piece(black_pieces[black_piece], moveid, color, captured_id)
                        pop_piece_out_lists(black_piece, 'black')
                    
                    black_options = get_both_options()[0]
                    white_options = get_both_options()[1]
                    
                    # pass play to black's turn
                    turn_step = 2
                    selection = 100
                    valid_moves = []
                    
                #add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            
                            # increment moves made counter!! 
                            moves_made_counter +=1
                            
                            # record previous coords to pass to record game moves
                            previous_white_locations.append(white_locations[selection])
                            
                            # change white locations selected coords
                            white_locations[selection] = click_coords
                            
                            # change boolean for selection to True if it's False
                            if(white_moved[selection]) == False:
                                white_moved[selection] = True
                            
                            # specify coords where castling happens
                            if click_coords == (1, 0):
                                rook_coords = (0, 0)
                            else: 
                                rook_coords = (7, 0)
                            
                            # get rook_index to update it
                            rook_index = white_locations.index(rook_coords)
                            
                            # record rook_index in previous_white_locations
                            previous_white_locations.append(white_locations[rook_index])
                            
                            # update king_index ? not sure if this is necessary after it probably happend on 468
                            king_index = click_coords
                            
                            # change rook index to castling move
                            white_locations[rook_index] = castling_moves[q][1]
                            
                            # log game move to gameMoves table
                            record_game_move(gameid,moves_made_counter,'white',selected_piece,previous_white_locations[-1],click_coords)
                            
                            # append to moves list
                            moves_made_list.append(all_moves.index('castle ' + str(rook_coords) + ' ' + str(king_index)))
                            
                            # display moves to right column
                            draw_moves_made(moves_made_list, 'white', moves_made_counter, column_two_counter, column_three_counter, column_four_counter)
                            
                            # log castling event
                            record_castling_event('white', moveid, str(white_locations[rook_index]), str(king_index))
                            
                            black_options = get_both_options()[0]
                            white_options = get_both_options()[1]
                            
                            # pass play to black's turn
                            turn_step = 2
                            selection = 100
                            valid_moves = []
            # black's turn 
            if turn_step > 1:
                
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white' # stops game play
                    
                if click_coords in black_locations:
                    # first click
                    selection = black_locations.index(click_coords)
                    
                    # check what piece is selected, so you can only draw castling if king is selected
                    selected_piece = black_pieces[selection]
                    
                    # second click
                    if turn_step == 2:
                        turn_step = 3
                        
                if click_coords in valid_moves and selection != 100:
                    black_ep = check_ep(black_locations[selection], click_coords)
                    
                    # record previous move to pass it to record game moves
                    previous_black_locations.append(black_locations[selection])
                    
                    #change black locations selected coords
                    black_locations[selection] = click_coords
                    
                    # change boolean for selection to True if it's False
                    if black_moved[selection]== False:
                        black_moved[selection] = True
                    
                    # increment moves made counter!! 
                    moves_made_counter += 1
                    
                    # column counter logic
                    if moves_made_counter == 33:
                        column_two_counter = 1
                    if moves_made_counter > 33 and moves_made_counter < 65:
                        column_two_counter +=1
                    if moves_made_counter == 65:
                        column_three_counter = 1
                    if moves_made_counter > 65 and moves_made_counter < 97:
                        column_three_counter +=1
                    if moves_made_counter == 97:
                        column_four_counter = 1
                    if moves_made_counter > 97 and moves_made_counter < 129:
                        column_four_counter +=1
                        
                    # log game move to gameMoves table
                    record_game_move(gameid,moves_made_counter,'black',selected_piece,previous_black_locations[-1],click_coords)
                    
                    # append to moves list
                    moves_made_list.append(all_moves.index(selected_piece +' '+ str(click_coords)))
                    
                    # display moves to right column
                    draw_moves_made(moves_made_list, 'black', moves_made_counter, column_two_counter, column_three_counter, column_four_counter)
                    
                    # record capture of white pieces
                    if click_coords in white_locations:
                        white_piece = white_locations.index(click_coords)
                        captured_pieces_black.append(white_pieces[white_piece])
                        color = 'black'
                        captured_id = str(white_pieces[white_piece])+str(moveid)+str(color)
                        record_captured_piece(white_pieces[white_piece], moveid, color, captured_id)
                        if white_pieces[white_piece] == 'king':
                            winner = 'black'
                        pop_piece_out_lists(white_piece, 'white')
                        
                    # En passant logic        
                    if click_coords == white_ep:
                        white_piece = white_locations.index((white_ep[0], white_ep[1]+1))
                        captured_pieces_black.append(white_pieces[white_piece])
                        color = 'black'
                        captured_id = str(white_pieces[black_piece])+str(moveid)+str(color)
                        record_captured_piece(white_pieces[white_piece], moveid, color, captured_id)
                        pop_piece_out_lists(white_piece, 'white')
                        
                    black_options = get_both_options()[0]
                    white_options = get_both_options()[1]
                    
                    # pass play to white's turn
                    turn_step = 0
                    selection = 100
                    valid_moves = []
                    #add option to castle
                elif selection != 100 and selected_piece == 'king':
                    for q in range(len(castling_moves)):
                        if click_coords == castling_moves[q][0]:
                            
                            # increment moves made counter!!
                            moves_made_counter +=1
                            
                            # record previous move to pass it to record game moves
                            previous_black_locations.append(black_locations[selection])
                            
                            # change black loations to selected coords
                            black_locations[selection] = click_coords
                            
                            # change boolean for selection to True if it's False
                            if black_moved[selection] == False:
                                black_moved[selection] = True
                            
                            # specify coords where castling happens
                            if click_coords == (1, 7):
                                rook_coords = (0, 7)
                            else: 
                                rook_coords = (7, 7)
                            
                            # get rook_index to update it
                            rook_index = black_locations.index(rook_coords)
                            
                            # record rook_index in previous_black_locations
                            previous_black_locations.append(black_locations[rook_index])
                            
                            # update king_index ? not sure if this is necessary after it probably happend on 578
                            king_index = click_coords
                            
                            # change rook index to castling move
                            black_locations[rook_index] = castling_moves[q][1]
                            
                            # log game move to gameMoves table
                            record_game_move(gameid,moves_made_counter,'black',selected_piece,previous_black_locations[-1],click_coords)
                            
                            # append to moves list
                            moves_made_list.append(all_moves.index('castle ' + str(rook_coords) + ' ' + str(king_index)))
                            
                            # display moves to right column
                            draw_moves_made(moves_made_list, 'black', moves_made_counter, column_two_counter, column_three_counter, column_four_counter)
                            
                            # log castling event
                            record_castling_event('black', moveid, str(black_locations[rook_index]), str(king_index))
                            
                            black_options = get_both_options()[0]
                            white_options = get_both_options()[1]
                            
                            #pass play to white's turn
                            turn_step = 0
                            selection = 100
                            valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                screen.fill('dark gray')
                game_over = False
                winner = ''
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                previous_white_locations = []
                white_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                previous_black_locations = []
                black_moved = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                captured_pieces_white = []
                captured_pieces_black = []
                turn_step = 0
                selection = 100
                valid_moves = []
                black_options = get_both_options()[0]
                white_options = get_both_options()[1]
                column_two_counter = 0
                column_three_counter = 0
                moves_made_counter = 0
                moves_made_list = []    
                create_new_game()
    if winner != '':
            game_over = True
            draw_game_over(winner)    
    pygame.display.flip()
pygame.quit()
