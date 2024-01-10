from constants import * 
from db_connection import connectionCredentials

def make_game_move(gameid,moves_made_counter,color,selected_piece,selection,click_coords):
    mydb = mysql.connector.connect(host=connectionCredentials()[0],user=connectionCredentials()[1],password=connectionCredentials()[2],database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO gameMoves (games_id, order_number, color, piece, start_pos, end_pos) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (gameid, moves_made_counter, color, selected_piece, selection, click_coords)
    mycursor.execute(sql,val)
    mydb.commit()