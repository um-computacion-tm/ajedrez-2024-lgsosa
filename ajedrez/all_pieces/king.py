from ajedrez.pieces import Piece
from directions import get_directions

class King(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♔", "♚", row, col)

    def basic_king_moves(self, row, col):
        directions = get_directions("king")
        return self.generate_moves(row, col, directions)

    def generate_moves(self, row, col, directions):
        moves = []
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            if 0 <= r < 8 and 0 <= c < 8:
                moves.append((r, c))
        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_king_moves(row, col)
