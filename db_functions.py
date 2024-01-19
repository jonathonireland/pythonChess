from constants import * 

def record_pawn_promotion(piece, moveid, color, promotion_id):
    values = (str(piece), str(moveid), str(color), str(promotion_id))
    try:
        mycursor.execute(record_pawn_promotion_sql, values)
        mydb.commit()
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

