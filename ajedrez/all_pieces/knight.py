from ajedrez.pieces import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_knight_moves(self, row, col):
        moves = []
        possible_moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
        for direction_r , direction_c in possible_moves:
            r , c = row + direction_r, col + direction_c
            if 0<= r < 8 and 0 <= c <=8: #in the board
                moves.append((r,c))
            
        return moves

#############