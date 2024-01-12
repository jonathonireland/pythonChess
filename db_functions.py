from constants import * 
from db_connection import connectionCredentials

def record_pawn_promotion(piece, moveid, color, promotion_id):
    mydb = mysql.connector.connect(host=connectionCredentials()[0], user=connectionCredentials()[1],password=connectionCredentials()[2], database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO gamePromotions (promotion_to_piece, game_moves_id, color, promotion_id) VALUES (%s, %s, %s, %s)"
    values = (str(piece), str(moveid), str(color), str(promotion_id))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()
        
def record_captured_piece(piece, moveid, color, captured_id):
    mydb = mysql.connector.connect(host=connectionCredentials()[0], user=connectionCredentials()[1],password=connectionCredentials()[2], database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO gameCaptures (captured_piece, game_moves_id, color, captured_id) VALUES (%s, %s, %s, %s)"
    values = (str(piece), str(moveid), str(color), str(captured_id))
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()