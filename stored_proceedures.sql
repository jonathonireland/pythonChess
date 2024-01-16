CREATE database pythonChess;
USE pythonChess;
CREATE TABLE games(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    game_name VARCHAR(255) NOT NULL,
    game_notes VARCHAR(255)
);
CREATE TABLE gameMoves(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    games_id INTEGER NOT NULL,
    order_number INTEGER NOT NULL,
    color VARCHAR(7) NOT NULL,
    piece VARCHAR(8) NOT NULL,
    start_pos VARCHAR(7) NOT NULL,
    end_pos VARCHAR(7) NOT NULL,
    FOREIGN KEY(games_id) REFERENCES games(id)
);
CREATE TABLE gameCaptures(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    captured_piece VARCHAR(7),
    game_moves_id INTEGER NOT NULL,
    color VARCHAR(7) NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
CREATE TABLE gamePromotions(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    promotion_to_piece VARCHAR(7),
    game_moves_id INTEGER NOT NULL,
    color VARCHAR(7) NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
CREATE TABLE gameCastling(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(7) NOT NULL,
    king_start_pos VARCHAR(7) NOT NULL,
    king_end_pos VARCHAR(7) NOT NULL,
    rook_start_pos VARCHAR(7) NOT NULL,
    rook_end_pos VARCHAR(7) NOT NULL,
    game_moves_id INTEGER NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);

SELECT * FROM games;
SELECT * FROM gamePromotions;
CREATE TABLE gamePromotions(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	promotion_to_piece VARCHAR(50),
    game_moves_id INTEGER NOT NULL,
    color VARCHAR(50) NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
SELECT * FROM gamePromotions;

CREATE TABLE gamePromotions(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,	
	promotion_to_piece VARCHAR(50),
    game_moves_id INTEGER NOT NULL,
    color VARCHAR(50) NOT NULL,
    promotion_id VARCHAR(60) UNIQUE NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
CREATE TABLE gameCaptures(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
	captured_piece VARCHAR(7),
	game_moves_id INTEGER NOT NULL,
	color VARCHAR(7) NOT NULL,
    captured_id VARCHAR(60) UNIQUE NOT NULL,
	FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
CREATE TABLE gameCastling(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(7) NOT NULL,
    rook_locations VARCHAR(70) NOT NULL,
    king_pos VARCHAR(70) NOT NULL,
    game_moves_id INTEGER NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);
CREATE TABLE gameChecks(
	id INTEGER AUTO_INCREMENT PRIMARY KEY,
    king_color VARCHAR(7) NOT NULL,
    king_pos VARCHAR(7) NOT NULL,
    game_moves_id INTEGER NOT NULL,
    gameCheckId VARCHAR(40) UNIQUE NOT NULL,
    FOREIGN KEY(game_moves_id) REFERENCES gameMoves(id)
);