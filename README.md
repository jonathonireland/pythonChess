<h1>Persistent Two-Player Chess</h1>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.36.21 AM.png" alt="black won the game! Persistent Two-Player Chess">

<h3>Pawn Promotions</h3>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.33.12 AM.png" alt="Pawn Promotion image">
<h3>Long Castling (on the queen's side)</h3>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.32.08 AM.png" alt="Long Castling" />
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
<li>adding (and inserting into) a "games" table for each game<br>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.56.49 AM.png" alt ="Select * from games ORDER BY id DESC LIMIT 10 shows that the games table is probably the least imaginative table but it is the base building block upon the games data is started with."/>
</li>
<li>adding (and inserting into) a "gameMoves" table for each move<br>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.53.33 AM.png" alt="Select * from gameMoves ORDER BY id DESC LIMIT 10 shows that game successfully creates a move associated with a specific game that includes the piece, starting position, ending position, and color."></li>
<li>adding (and inserting into) a "gameCaptures" table for each capture<br>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.44.15 AM.png" alt="Select * From gameCaptures limit 10 shows that game successfully logs captures when playing the game." /></li> 
<li>adding (and inserting into) a "gameChecks" table for each check
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 9.41.52 AM.png" alt="inserts completed in gameChecks"/></li>
<li>adding (and inserting into) a "gamePromotions" table for each pawn promotion, there is room for improvement here, the ids for the promotion do not increment as they should due to the game looping while the insert is happening. Still working through these issues.<br>
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot%202024-01-16%20at%2010.00.58%20AM.png" alt="select * from gamePromotions ORDER BY id DESC LIMIT 10 shows that there is room for improvement here, the ids for the promotion do not increment as they should due to the game looping while the insert is happening. " /></li>
<li>adding (and inserting into) a "gameCastling" table for each castle. There is room for improvement here, would like to capture the starting position of the king and rook and then their position after they complete the castle maneuver<br> 
<img src="https://www.jonathonireland.com/resume/data/files/Screenshot 2024-01-16 at 10.04.40 AM.png" alt="select * from gameCastling ORDER BY id DESC LIMIT 10 shows that castle moves are captured and associated with a game move id." /></li>
<li>adding (and inserting into) a "gameWinners" table for every completed game and incompleted game.</li>
</ul>
<h3>Development plans:</h3>
<ol>
<li>Completed: Connect pygame to persistent data.</li>
<li>Completed: Save each game to a games table assigned last game id to global gameid variable.</li>
<li>Completed: Save each moves made to a gameMoves table.</li>
<li>Completed: Save each pawn promotion to a gamePromotions table.</li>
<li>Completed: Save each capture to a gameCaptures table.</li>
<li>Completed: Save each castling instance to a gameCastling table.</li>
<li>Completed: Save each check instance to a gameChecks table.</li>
<li>Completed: Fix game move quirks created from adding castling to moves types.</li>
<li>Completed: Replace old ugly game pieces with glossy nice ones.</li>
<li>Fix Game reset after forfeit pieces do not reset as expected.</li>
<li>Improve Readme file 100X over</li>
<li>Clean up code.</li>
<li>Record game winners to a table (moves? or it's own table).</li>
<li>Add more features based on database connection.</li>
</ol>

