from constants import * 
from db_connection import connectionCredentials

def record_game_move(gameid,moves_made_counter,color,selected_piece,selection,click_coords):
    mydb = mysql.connector.connect(host=connectionCredentials()[0],user=connectionCredentials()[1],password=connectionCredentials()[2],database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO gameMoves (games_id, order_number, color, piece, start_pos, end_pos) VALUES ('"+str(gameid)+"', '"+str(moves_made_counter)+"', '"+color+"', '"+str(selected_piece)+"', '"+str(selection)+"', '"+str(click_coords)+"')"
    try:
        mycursor.execute(sql)
        mydb.commit()
    except:
        mydb.rollback()
