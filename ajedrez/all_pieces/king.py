from ajedrez.pieces import Piece, Directions

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♕", "♛", row, col)

    def basic_queen_moves(self, row, col):
        moves = []
        directions = Directions.diagonal() + Directions.straight()  # Usar las direcciones
        
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            while 0 <= r < 8 and 0 <= c < 8:
                moves.append((r, c))
                r += direction_r
                c += direction_c

        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_queen_moves(row, col)
