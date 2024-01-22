from constants import * 


## RECORD or INSERT FUNCTIONAL QUERIES
def record_pawn_promotion(piece, moveid, color, promotion_id):
    values = (str(piece), str(moveid), str(color), str(promotion_id))
    try:
        mycursor.execute(record_pawn_promotion_sql, values)
        mydb.commit()
        global promo_events
        promo_events.append(promotion_id)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


def record_captured_piece(piece, moveid, color, captured_id):
    values = (str(piece), str(moveid), str(color), str(captured_id))
    try:
        mycursor.execute(record_captures_sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


def record_castling_event(color, moveid, rook_locations, king_pos):
    values = (str(color), str(rook_locations), str(king_pos), str(moveid))
    try:
        mycursor.execute(record_castling_event_sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()
        
        
def record_check_event(color, king_location, moveid, game_check_id):
    values = (str(color), str(king_location), str(moveid), str(game_check_id)) 
    try:
        mycursor.execute(record_check_event_sql, values)
        mydb.commit()
        global check_events
        check_events.append(game_check_id)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


## FETCH or SELECT FUNCTIONAL QUERIES

def fetch_game_move(game_id, moves_made_counter):
    try:
        mycursor.execute(fetch_game_move_sql, (game_id, moves_made_counter))
        move = mycursor.fetchall()
        return move
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()
        return []
    
def fetch_game_moves(game_id):
    try:
        mycursor.execute(fetch_game_moves_sql, (game_id,))
        moves = mycursor.fetchall()
        return moves
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()
        return []