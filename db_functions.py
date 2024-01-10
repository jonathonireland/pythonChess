from constants import * 
from db_connection import connectionCredentials

def create_new_game():
    mydb = mysql.connector.connect(host=connectionCredentials()[0],user=connectionCredentials()[1],password=connectionCredentials()[2],database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO games (game_name, game_notes) VALUES (%s, %s)"
    val = ("newGame", "initial attempt")
    mycursor.execute(sql, val)
    mydb.commit()
    global gameid
    gameid = mycursor.lastrowid
    print(str(gameid) + "game id has a value")

def record_game_move(gameid,moves_made_counter,color,selected_piece,selection,click_coords):
    mydb = mysql.connector.connect(host=connectionCredentials()[0],user=connectionCredentials()[1],password=connectionCredentials()[2],database=connectionCredentials()[3])
    mycursor = mydb.cursor()
    sql = "INSERT INTO gameMoves (games_id, order_number, color, piece, start_pos, end_pos) VALUES ('"+str(gameid)+"', '"+str(moves_made_counter)+"', '"+color+"', '"+str(selected_piece)+"', '"+str(selection)+"', '"+str(click_coords)+"')"
    try:
        # Executing the SQL command
        mycursor.execute(sql)
        # Commit your changes in the database
        mydb.commit()
    except:
        # Rolling back in case of error
        mydb.rollback()
