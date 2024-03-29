<h1>Data Persistent Two-Player Chess</h1>
<h2>Project Synopsis</h2>
<p>Now that data is captured for every aspect for a chess game, I am going to continue pursuing short term development plans.</p>
<h3>Pawn Promotions</h3>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.33.12 AM.png" alt="Pawn Promotion image">
<h3>Long Castling (on the queen's side)</h3>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.32.08 AM.png" alt="Long Castling" />
<h3>Both Castle Options</h3>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-17 at 10.11.06 AM.png" alt="Picture shows white side of the board with both castle options" />
<h3>Shows 128 Moves</h3>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-17 at 10.28.49 AM.png" alt="Shows 128 Moves on the right rectangle box" />
<h3>Game Over</h3>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.36.21 AM.png" alt="black won the game! Persistent Two-Player Chess">
<h3>En passant</h3>
<p>En Passant allows a pawn to capture after moving diagonally behind an opponents piece. The highlighted square in the graphic here shows that the white pawn can move diagonally and then capture the black pawn behind it.</p>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-23 at 12.44.54 PM.png" alt="En Passant allows a pawn to capture after moving diagonally behind an opponents piece. The highlighted square in the graphic here shows that the white pawn can move diagonally and then capture the black pawn behind it." />
<p>This screen shot shows that the captured black pawn is no longer on the board after the en passant move takes place.</p>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-23 at 12.45.09 PM.png" alt="This screen shot shows that the captured black pawn is no longer on the board after the en passant move takes place."/>
<p>This Pygame development I started in December of 2023 because of an interest in learning Python (and) I have always thought Chess was fun. It quickly became an obsession in completing the tutorials below... It has not stopped there though, I don't know where this will end up, it's only for fun, so it doesn't have to stop.</p>
<ol>
<li><a href="https://www.youtube.com/watch?v=X-e0jk4I938&t=7481s">https://www.youtube.com/watch?v=X-e0jk4I938&t=7481s</a></li>
<li><a href="https://www.youtube.com/watch?v=s2Dd_obh3fM&t=134s">https://www.youtube.com/watch?v=s2Dd_obh3fM&t=134s</a></li>
</ol>
<p>Those two tutorials were a great foundation to begin experimentation and learning in Python. Once they were completed, I began to start coding ideas of my own for the game, and I still am developing new features.</p>
<h2>Working through development plans.</h2>
<p>Obvious changes in the game's interface:</p>
<ul>
<li>listing out the moves made through the game next to the pieces that were captured</li> 
</ul>
<p>New coding features include: </p>
<ul>
<li>adding (and inserting into) a "games" table for each game.<br>Select * from games ORDER BY id DESC LIMIT 10 shows that the games table is probably the least imaginative table but it is the base building block upon the games data is started with.<br>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.56.49 AM.png" alt ="Select * from games ORDER BY id DESC LIMIT 10 shows that the games table is probably the least imaginative table but it is the base building block upon the games data is started with."/>
</li>
<li>adding (and inserting into) a "gameMoves" table for each move<br>Select * from gameMoves ORDER BY id DESC LIMIT 10 shows that game successfully creates a move associated with a specific game that includes the piece, starting position, ending position, and color.<br>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.53.33 AM.png" alt="Select * from gameMoves ORDER BY id DESC LIMIT 10 shows that game successfully creates a move associated with a specific game that includes the piece, starting position, ending position, and color."></li>
<li>adding (and inserting into) a "gameCaptures" table for each capture<br>Select * From gameCaptures limit 10 shows that game successfully logs captures when playing the game.<br>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.44.15 AM.png" alt="Select * From gameCaptures limit 10 shows that game successfully logs captures when playing the game." /></li> 
<li>adding (and inserting into) a "gameChecks" table for each check
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 9.41.52 AM.png" alt="inserts completed in gameChecks"/></li>
<li>adding (and inserting into) a "gamePromotions" table for each pawn promotion.<br>select * from gamePromotions ORDER BY id DESC LIMIT 10 shows that there is room for improvement here, the ids for the promotion do not increment as they should due to the game looping while the insert is happening.<br>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot%202024-01-16%20at%2010.00.58%20AM.png" alt="select * from gamePromotions ORDER BY id DESC LIMIT 10 shows that there is room for improvement here, the ids for the promotion do not increment as they should due to the game looping while the insert is happening. " /></li>
<li>adding (and inserting into) a "gameCastling" table for each castle. There is room for improvement here, would like to (possibly) capture the starting position of the king and rook and then their position after they complete the castle maneuver<br>select * from gameCastling ORDER BY id DESC LIMIT 10 shows that castle moves are captured and associated with a game move id.<br>
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-16 at 10.04.40 AM.png" alt="select * from gameCastling ORDER BY id DESC LIMIT 10 shows that castle moves are captured and associated with a game move id." /></li>
<li>adding (and inserting into) a "gamesCompleted" table for every completed game.
<img src="https://jonathonireland.com/backup_old_site/resume/data/files/Screenshot 2024-01-22 at 11.11.51 PM.png" alt="select * from gamesCompleted; shows that the game is recording completd games that result in a winner." />
</li>
<li>Fixed Game Reset after Forfeit button is clicked!!</li>
</ul>
<h3>Short-term Development plans:</h3>
<ol>
<li>Load a list of games from persistent Data</li>
<li>Select a game from the list and load all game moves played already.</li>
<li>Give option to save game or delete it.</li>
<li>Give an option to re-name a game.</li>
<li>Give an option to add notes to the game.</li>
</ol>
<h2>To run this on your local (on Mac OS 13 or newer)</h2>
<ol>
<li>Install Python 3.12.0 or newer.</li>
<li>Install MySQL 8.0.34 or newer.</li>
<li>Create a db_connection.py file in the root of the pythonchess folder.</li>
<li>Copy and paste stored_procedures.sql and run the structured queries.</li>
<li>Run the main.py file to start the game.</li>
</ol>
