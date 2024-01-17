from constants import * 

def run_once(f):
    def wrapper(*args):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args)
        wrapper.has_run = False
    return wrapper

# @run_once
def record_pawn_promotion(piece, moveid, color, promotion_id):
  #  has_run = False
    sql = "INSERT INTO gamePromotions (promotion_to_piece, game_moves_id, color, promotion_id) VALUES (%s, %s, %s, %s)"
    values = (str(piece), str(moveid), str(color), str(promotion_id))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
   #     has_run = True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


# @run_once        
def record_captured_piece(piece, moveid, color, captured_id):
    #has_run = False
    sql = "INSERT INTO gameCaptures (captured_piece, game_moves_id, color, captured_id) VALUES (%s, %s, %s, %s)"
    values = (str(piece), str(moveid), str(color), str(captured_id))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
  #      has_run = True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


# @run_once      
def record_castling_event(color, moveid, rook_locations, king_pos):
   # has_run = False
    sql = "INSERT INTO gameCastling (color, rook_locations, king_pos, game_moves_id) VALUES (%s, %s, %s, %s)"
    values = (str(color), str(rook_locations), str(king_pos), str(moveid))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
  #      has_run = True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


#@run_once
def record_check_event(color, king_location, moveid, game_check_id):
    # has_run = False
    sql = "INSERT INTO gameChecks (king_color, king_pos, game_moves_id, gameCheckId) VALUES (%s, %s, %s, %s)"
    values = (str(color), str(king_location), str(moveid), str(game_check_id)) 
    try:
        mycursor.execute(sql, values)
        mydb.commit()
     #   has_run = True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()


def record_game_over(gameid, moveid, winner, gameCompletedKey):
    sql = "INSERT INTO gamesCompleted (gameid, game_moves_id, winner, gameCompletedKey) VALUES(%s, %s, %s, %s)"
    values = (str(gameid), str(moveid), str(winner), str(gameCompletedKey))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()