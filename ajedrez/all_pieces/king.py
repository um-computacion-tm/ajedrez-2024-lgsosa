from ajedrez.pieces import Piece

class King(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♔", "♚", row, col)

    def basic_king_moves(self, row, col):
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),         ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        for direction_row, direction_col in directions:
            r, c = row + direction_row, col + direction_col

            if self.is_within_bounds(r, c):
                moves.append((r, c))
                
        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_king_moves(row, col)
