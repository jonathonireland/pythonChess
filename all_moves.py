all_moves = ['rook (0, 0)', 'rook (0, 1)', 'rook (0, 2)', 'rook (0, 3)', 'rook (0, 4)', 'rook (0, 5)', 'rook (0, 6)', 'rook (0, 7)', 
    'rook (1, 0)', 'rook (1, 1)', 'rook (1, 2)', 'rook (1, 3)', 'rook (1, 4)', 'rook (1, 5)', 'rook (1, 6)', 'rook (1, 7)', 
    'rook (2, 0)', 'rook (2, 1)', 'rook (2, 2)', 'rook (2, 3)', 'rook (2, 4)', 'rook (2, 5)', 'rook (2, 6)', 'rook (2, 7)', 
    'rook (3, 0)', 'rook (3, 1)', 'rook (3, 2)', 'rook (3, 3)', 'rook (3, 4)', 'rook (3, 5)', 'rook (3, 6)', 'rook (3, 7)', 
    'rook (4, 0)', 'rook (4, 1)', 'rook (4, 2)', 'rook (4, 3)', 'rook (4, 4)', 'rook (4, 5)', 'rook (4, 6)', 'rook (4, 7)', 
    'rook (5, 0)', 'rook (5, 1)', 'rook (5, 2)', 'rook (5, 3)', 'rook (5, 4)', 'rook (5, 5)', 'rook (5, 6)', 'rook (5, 7)', 
    'rook (6, 0)', 'rook (6, 1)', 'rook (6, 2)', 'rook (6, 3)', 'rook (6, 4)', 'rook (6, 5)', 'rook (6, 6)', 'rook (6, 7)', 
    'rook (7, 0)', 'rook (7, 1)', 'rook (7, 2)', 'rook (7, 3)', 'rook (7, 4)', 'rook (7, 5)', 'rook (7, 6)', 'rook (7, 7)',
    'knight (0, 0)', 'knight (0, 1)', 'knight (0, 2)', 'knight (0, 3)', 'knight (0, 4)', 'knight (0, 5)', 'knight (0, 6)', 'knight (0, 7)', 
    'knight (1, 0)', 'knight (1, 1)', 'knight (1, 2)', 'knight (1, 3)', 'knight (1, 4)', 'knight (1, 5)', 'knight (1, 6)', 'knight (1, 7)', 
    'knight (2, 0)', 'knight (2, 1)', 'knight (2, 2)', 'knight (2, 3)', 'knight (2, 4)', 'knight (2, 5)', 'knight (2, 6)', 'knight (2, 7)', 
    'knight (3, 0)', 'knight (3, 1)', 'knight (3, 2)', 'knight (3, 3)', 'knight (3, 4)', 'knight (3, 5)', 'knight (3, 6)', 'knight (3, 7)', 
    'knight (4, 0)', 'knight (4, 1)', 'knight (4, 2)', 'knight (4, 3)', 'knight (4, 4)', 'knight (4, 5)', 'knight (4, 6)', 'knight (4, 7)', 
    'knight (5, 0)', 'knight (5, 1)', 'knight (5, 2)', 'knight (5, 3)', 'knight (5, 4)', 'knight (5, 5)', 'knight (5, 6)', 'knight (5, 7)', 
    'knight (6, 0)', 'knight (6, 1)', 'knight (6, 2)', 'knight (6, 3)', 'knight (6, 4)', 'knight (6, 5)', 'knight (6, 6)', 'knight (6, 7)', 
    'knight (7, 0)', 'knight (7, 1)', 'knight (7, 2)', 'knight (7, 3)', 'knight (7, 4)', 'knight (7, 5)', 'knight (7, 6)', 'knight (7, 7)',
    'bishop (0, 0)', 'bishop (0, 1)', 'bishop (0, 2)', 'bishop (0, 3)', 'bishop (0, 4)', 'bishop (0, 5)', 'bishop (0, 6)', 'bishop (0, 7)', 
    'bishop (1, 0)', 'bishop (1, 1)', 'bishop (1, 2)', 'bishop (1, 3)', 'bishop (1, 4)', 'bishop (1, 5)', 'bishop (1, 6)', 'bishop (1, 7)', 
    'bishop (2, 0)', 'bishop (2, 1)', 'bishop (2, 2)', 'bishop (2, 3)', 'bishop (2, 4)', 'bishop (2, 5)', 'bishop (2, 6)', 'bishop (2, 7)', 
    'bishop (3, 0)', 'bishop (3, 1)', 'bishop (3, 2)', 'bishop (3, 3)', 'bishop (3, 4)', 'bishop (3, 5)', 'bishop (3, 6)', 'bishop (3, 7)', 
    'bishop (4, 0)', 'bishop (4, 1)', 'bishop (4, 2)', 'bishop (4, 3)', 'bishop (4, 4)', 'bishop (4, 5)', 'bishop (4, 6)', 'bishop (4, 7)', 
    'bishop (5, 0)', 'bishop (5, 1)', 'bishop (5, 2)', 'bishop (5, 3)', 'bishop (5, 4)', 'bishop (5, 5)', 'bishop (5, 6)', 'bishop (5, 7)', 
    'bishop (6, 0)', 'bishop (6, 1)', 'bishop (6, 2)', 'bishop (6, 3)', 'bishop (6, 4)', 'bishop (6, 5)', 'bishop (6, 6)', 'bishop (6, 7)', 
    'bishop (7, 0)', 'bishop (7, 1)', 'bishop (7, 2)', 'bishop (7, 3)', 'bishop (7, 4)', 'bishop (7, 5)', 'bishop (7, 6)', 'bishop (7, 7)',
    'king (0, 0)', 'king (0, 1)', 'king (0, 2)', 'king (0, 3)', 'king (0, 4)', 'king (0, 5)', 'king (0, 6)', 'king (0, 7)', 
    'king (1, 0)', 'king (1, 1)', 'king (1, 2)', 'king (1, 3)', 'king (1, 4)', 'king (1, 5)', 'king (1, 6)', 'king (1, 7)', 
    'king (2, 0)', 'king (2, 1)', 'king (2, 2)', 'king (2, 3)', 'king (2, 4)', 'king (2, 5)', 'king (2, 6)', 'king (2, 7)', 
    'king (3, 0)', 'king (3, 1)', 'king (3, 2)', 'king (3, 3)', 'king (3, 4)', 'king (3, 5)', 'king (3, 6)', 'king (3, 7)', 
    'king (4, 0)', 'king (4, 1)', 'king (4, 2)', 'king (4, 3)', 'king (4, 4)', 'king (4, 5)', 'king (4, 6)', 'king (4, 7)', 
    'king (5, 0)', 'king (5, 1)', 'king (5, 2)', 'king (5, 3)', 'king (5, 4)', 'king (5, 5)', 'king (5, 6)', 'king (5, 7)', 
    'king (6, 0)', 'king (6, 1)', 'king (6, 2)', 'king (6, 3)', 'king (6, 4)', 'king (6, 5)', 'king (6, 6)', 'king (6, 7)', 
    'king (7, 0)', 'king (7, 1)', 'king (7, 2)', 'king (7, 3)', 'king (7, 4)', 'king (7, 5)', 'king (7, 6)', 'king (7, 7)',
    'queen (0, 0)', 'queen (0, 1)', 'queen (0, 2)', 'queen (0, 3)', 'queen (0, 4)', 'queen (0, 5)', 'queen (0, 6)', 'queen (0, 7)', 
    'queen (1, 0)', 'queen (1, 1)', 'queen (1, 2)', 'queen (1, 3)', 'queen (1, 4)', 'queen (1, 5)', 'queen (1, 6)', 'queen (1, 7)', 
    'queen (2, 0)', 'queen (2, 1)', 'queen (2, 2)', 'queen (2, 3)', 'queen (2, 4)', 'queen (2, 5)', 'queen (2, 6)', 'queen (2, 7)', 
    'queen (3, 0)', 'queen (3, 1)', 'queen (3, 2)', 'queen (3, 3)', 'queen (3, 4)', 'queen (3, 5)', 'queen (3, 6)', 'queen (3, 7)', 
    'queen (4, 0)', 'queen (4, 1)', 'queen (4, 2)', 'queen (4, 3)', 'queen (4, 4)', 'queen (4, 5)', 'queen (4, 6)', 'queen (4, 7)', 
    'queen (5, 0)', 'queen (5, 1)', 'queen (5, 2)', 'queen (5, 3)', 'queen (5, 4)', 'queen (5, 5)', 'queen (5, 6)', 'queen (5, 7)', 
    'queen (6, 0)', 'queen (6, 1)', 'queen (6, 2)', 'queen (6, 3)', 'queen (6, 4)', 'queen (6, 5)', 'queen (6, 6)', 'queen (6, 7)', 
    'queen (7, 0)', 'queen (7, 1)', 'queen (7, 2)', 'queen (7, 3)', 'queen (7, 4)', 'queen (7, 5)', 'queen (7, 6)', 'queen (7, 7)',
    'pawn (0, 0)', 'pawn (0, 1)', 'pawn (0, 2)', 'pawn (0, 3)', 'pawn (0, 4)', 'pawn (0, 5)', 'pawn (0, 6)', 'pawn (0, 7)', 
    'pawn (1, 0)', 'pawn (1, 1)', 'pawn (1, 2)', 'pawn (1, 3)', 'pawn (1, 4)', 'pawn (1, 5)', 'pawn (1, 6)', 'pawn (1, 7)', 
    'pawn (2, 0)', 'pawn (2, 1)', 'pawn (2, 2)', 'pawn (2, 3)', 'pawn (2, 4)', 'pawn (2, 5)', 'pawn (2, 6)', 'pawn (2, 7)', 
    'pawn (3, 0)', 'pawn (3, 1)', 'pawn (3, 2)', 'pawn (3, 3)', 'pawn (3, 4)', 'pawn (3, 5)', 'pawn (3, 6)', 'pawn (3, 7)', 
    'pawn (4, 0)', 'pawn (4, 1)', 'pawn (4, 2)', 'pawn (4, 3)', 'pawn (4, 4)', 'pawn (4, 5)', 'pawn (4, 6)', 'pawn (4, 7)', 
    'pawn (5, 0)', 'pawn (5, 1)', 'pawn (5, 2)', 'pawn (5, 3)', 'pawn (5, 4)', 'pawn (5, 5)', 'pawn (5, 6)', 'pawn (5, 7)', 
    'pawn (6, 0)', 'pawn (6, 1)', 'pawn (6, 2)', 'pawn (6, 3)', 'pawn (6, 4)', 'pawn (6, 5)', 'pawn (6, 6)', 'pawn (6, 7)', 
    'pawn (7, 0)', 'pawn (7, 1)', 'pawn (7, 2)', 'pawn (7, 3)', 'pawn (7, 4)', 'pawn (7, 5)', 'pawn (7, 6)', 'pawn (7, 7)',
    'rook (0, 0)', 'rook (0, 1)', 'rook (0, 2)', 'rook (0, 3)', 'rook (0, 4)', 'rook (0, 5)', 'rook (0, 6)', 'rook (0, 7)', 
    'rook (1, 0)', 'rook (1, 1)', 'rook (1, 2)', 'rook (1, 3)', 'rook (1, 4)', 'rook (1, 5)', 'rook (1, 6)', 'rook (1, 7)', 
    'rook (2, 0)', 'rook (2, 1)', 'rook (2, 2)', 'rook (2, 3)', 'rook (2, 4)', 'rook (2, 5)', 'rook (2, 6)', 'rook (2, 7)', 
    'rook (3, 0)', 'rook (3, 1)', 'rook (3, 2)', 'rook (3, 3)', 'rook (3, 4)', 'rook (3, 5)', 'rook (3, 6)', 'rook (3, 7)', 
    'rook (4, 0)', 'rook (4, 1)', 'rook (4, 2)', 'rook (4, 3)', 'rook (4, 4)', 'rook (4, 5)', 'rook (4, 6)', 'rook (4, 7)', 
    'rook (5, 0)', 'rook (5, 1)', 'rook (5, 2)', 'rook (5, 3)', 'rook (5, 4)', 'rook (5, 5)', 'rook (5, 6)', 'rook (5, 7)', 
    'rook (6, 0)', 'rook (6, 1)', 'rook (6, 2)', 'rook (6, 3)', 'rook (6, 4)', 'rook (6, 5)', 'rook (6, 6)', 'rook (6, 7)', 
    'rook (7, 0)', 'rook (7, 1)', 'rook (7, 2)', 'rook (7, 3)', 'rook (7, 4)', 'rook (7, 5)', 'rook (7, 6)', 'rook (7, 7)',
    'knight (0, 0)', 'knight (0, 1)', 'knight (0, 2)', 'knight (0, 3)', 'knight (0, 4)', 'knight (0, 5)', 'knight (0, 6)', 'knight (0, 7)', 
    'knight (1, 0)', 'knight (1, 1)', 'knight (1, 2)', 'knight (1, 3)', 'knight (1, 4)', 'knight (1, 5)', 'knight (1, 6)', 'knight (1, 7)', 
    'knight (2, 0)', 'knight (2, 1)', 'knight (2, 2)', 'knight (2, 3)', 'knight (2, 4)', 'knight (2, 5)', 'knight (2, 6)', 'knight (2, 7)', 
    'knight (3, 0)', 'knight (3, 1)', 'knight (3, 2)', 'knight (3, 3)', 'knight (3, 4)', 'knight (3, 5)', 'knight (3, 6)', 'knight (3, 7)', 
    'knight (4, 0)', 'knight (4, 1)', 'knight (4, 2)', 'knight (4, 3)', 'knight (4, 4)', 'knight (4, 5)', 'knight (4, 6)', 'knight (4, 7)', 
    'knight (5, 0)', 'knight (5, 1)', 'knight (5, 2)', 'knight (5, 3)', 'knight (5, 4)', 'knight (5, 5)', 'knight (5, 6)', 'knight (5, 7)', 
    'knight (6, 0)', 'knight (6, 1)', 'knight (6, 2)', 'knight (6, 3)', 'knight (6, 4)', 'knight (6, 5)', 'knight (6, 6)', 'knight (6, 7)', 
    'knight (7, 0)', 'knight (7, 1)', 'knight (7, 2)', 'knight (7, 3)', 'knight (7, 4)', 'knight (7, 5)', 'knight (7, 6)', 'knight (7, 7)',
    'bishop (0, 0)', 'bishop (0, 1)', 'bishop (0, 2)', 'bishop (0, 3)', 'bishop (0, 4)', 'bishop (0, 5)', 'bishop (0, 6)', 'bishop (0, 7)', 
    'bishop (1, 0)', 'bishop (1, 1)', 'bishop (1, 2)', 'bishop (1, 3)', 'bishop (1, 4)', 'bishop (1, 5)', 'bishop (1, 6)', 'bishop (1, 7)', 
    'bishop (2, 0)', 'bishop (2, 1)', 'bishop (2, 2)', 'bishop (2, 3)', 'bishop (2, 4)', 'bishop (2, 5)', 'bishop (2, 6)', 'bishop (2, 7)', 
    'bishop (3, 0)', 'bishop (3, 1)', 'bishop (3, 2)', 'bishop (3, 3)', 'bishop (3, 4)', 'bishop (3, 5)', 'bishop (3, 6)', 'bishop (3, 7)', 
    'bishop (4, 0)', 'bishop (4, 1)', 'bishop (4, 2)', 'bishop (4, 3)', 'bishop (4, 4)', 'bishop (4, 5)', 'bishop (4, 6)', 'bishop (4, 7)', 
    'bishop (5, 0)', 'bishop (5, 1)', 'bishop (5, 2)', 'bishop (5, 3)', 'bishop (5, 4)', 'bishop (5, 5)', 'bishop (5, 6)', 'bishop (5, 7)', 
    'bishop (6, 0)', 'bishop (6, 1)', 'bishop (6, 2)', 'bishop (6, 3)', 'bishop (6, 4)', 'bishop (6, 5)', 'bishop (6, 6)', 'bishop (6, 7)', 
    'bishop (7, 0)', 'bishop (7, 1)', 'bishop (7, 2)', 'bishop (7, 3)', 'bishop (7, 4)', 'bishop (7, 5)', 'bishop (7, 6)', 'bishop (7, 7)',
    'king (0, 0)', 'king (0, 1)', 'king (0, 2)', 'king (0, 3)', 'king (0, 4)', 'king (0, 5)', 'king (0, 6)', 'king (0, 7)', 
    'king (1, 0)', 'king (1, 1)', 'king (1, 2)', 'king (1, 3)', 'king (1, 4)', 'king (1, 5)', 'king (1, 6)', 'king (1, 7)', 
    'king (2, 0)', 'king (2, 1)', 'king (2, 2)', 'king (2, 3)', 'king (2, 4)', 'king (2, 5)', 'king (2, 6)', 'king (2, 7)', 
    'king (3, 0)', 'king (3, 1)', 'king (3, 2)', 'king (3, 3)', 'king (3, 4)', 'king (3, 5)', 'king (3, 6)', 'king (3, 7)', 
    'king (4, 0)', 'king (4, 1)', 'king (4, 2)', 'king (4, 3)', 'king (4, 4)', 'king (4, 5)', 'king (4, 6)', 'king (4, 7)', 
    'king (5, 0)', 'king (5, 1)', 'king (5, 2)', 'king (5, 3)', 'king (5, 4)', 'king (5, 5)', 'king (5, 6)', 'king (5, 7)', 
    'king (6, 0)', 'king (6, 1)', 'king (6, 2)', 'king (6, 3)', 'king (6, 4)', 'king (6, 5)', 'king (6, 6)', 'king (6, 7)', 
    'king (7, 0)', 'king (7, 1)', 'king (7, 2)', 'king (7, 3)', 'king (7, 4)', 'king (7, 5)', 'king (7, 6)', 'king (7, 7)',
    'queen (0, 0)', 'queen (0, 1)', 'queen (0, 2)', 'queen (0, 3)', 'queen (0, 4)', 'queen (0, 5)', 'queen (0, 6)', 'queen (0, 7)', 
    'queen (1, 0)', 'queen (1, 1)', 'queen (1, 2)', 'queen (1, 3)', 'queen (1, 4)', 'queen (1, 5)', 'queen (1, 6)', 'queen (1, 7)', 
    'queen (2, 0)', 'queen (2, 1)', 'queen (2, 2)', 'queen (2, 3)', 'queen (2, 4)', 'queen (2, 5)', 'queen (2, 6)', 'queen (2, 7)', 
    'queen (3, 0)', 'queen (3, 1)', 'queen (3, 2)', 'queen (3, 3)', 'queen (3, 4)', 'queen (3, 5)', 'queen (3, 6)', 'queen (3, 7)', 
    'queen (4, 0)', 'queen (4, 1)', 'queen (4, 2)', 'queen (4, 3)', 'queen (4, 4)', 'queen (4, 5)', 'queen (4, 6)', 'queen (4, 7)', 
    'queen (5, 0)', 'queen (5, 1)', 'queen (5, 2)', 'queen (5, 3)', 'queen (5, 4)', 'queen (5, 5)', 'queen (5, 6)', 'queen (5, 7)', 
    'queen (6, 0)', 'queen (6, 1)', 'queen (6, 2)', 'queen (6, 3)', 'queen (6, 4)', 'queen (6, 5)', 'queen (6, 6)', 'queen (6, 7)', 
    'queen (7, 0)', 'queen (7, 1)', 'queen (7, 2)', 'queen (7, 3)', 'queen (7, 4)', 'queen (7, 5)', 'queen (7, 6)', 'queen (7, 7)',
    'pawn (0, 0)', 'pawn (0, 1)', 'pawn (0, 2)', 'pawn (0, 3)', 'pawn (0, 4)', 'pawn (0, 5)', 'pawn (0, 6)', 'pawn (0, 7)', 
    'pawn (1, 0)', 'pawn (1, 1)', 'pawn (1, 2)', 'pawn (1, 3)', 'pawn (1, 4)', 'pawn (1, 5)', 'pawn (1, 6)', 'pawn (1, 7)', 
    'pawn (2, 0)', 'pawn (2, 1)', 'pawn (2, 2)', 'pawn (2, 3)', 'pawn (2, 4)', 'pawn (2, 5)', 'pawn (2, 6)', 'pawn (2, 7)', 
    'pawn (3, 0)', 'pawn (3, 1)', 'pawn (3, 2)', 'pawn (3, 3)', 'pawn (3, 4)', 'pawn (3, 5)', 'pawn (3, 6)', 'pawn (3, 7)', 
    'pawn (4, 0)', 'pawn (4, 1)', 'pawn (4, 2)', 'pawn (4, 3)', 'pawn (4, 4)', 'pawn (4, 5)', 'pawn (4, 6)', 'pawn (4, 7)', 
    'pawn (5, 0)', 'pawn (5, 1)', 'pawn (5, 2)', 'pawn (5, 3)', 'pawn (5, 4)', 'pawn (5, 5)', 'pawn (5, 6)', 'pawn (5, 7)', 
    'pawn (6, 0)', 'pawn (6, 1)', 'pawn (6, 2)', 'pawn (6, 3)', 'pawn (6, 4)', 'pawn (6, 5)', 'pawn (6, 6)', 'pawn (6, 7)', 
    'pawn (7, 0)', 'pawn (7, 1)', 'pawn (7, 2)', 'pawn (7, 3)', 'pawn (7, 4)', 'pawn (7, 5)', 'pawn (7, 6)', 'pawn (7, 7)',
    'castle (0, 0) (1, 0)', 'castle (2, 0) (1, 0)', 'castle (2, 7) (1, 7)', 'castle (4, 7) (5, 7)', 'castle (4, 0) (5, 0)',
    'castle (0, 7) (1, 7)', 'castle (7, 0) (5, 0)', 'castle (7, 7) (5, 7)']