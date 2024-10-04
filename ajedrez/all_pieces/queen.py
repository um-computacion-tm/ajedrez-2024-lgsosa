from ajedrez.pieces import Piece
from directions import get_directions

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♕", "♛", row, col)

    def basic_queen_moves(self, row, col):
        moves = []
        directions = get_directions("queen")
        moves.extend(self.generate_moves(row, col, directions))
        return moves

    def generate_moves(self, row, col, directions):
        moves = []
        for direction_r, direction_c in directions:
            r, c = row, col
            while 0 <= r < 8 and 0 <= c < 8:
                r += direction_r
                c += direction_c
                if 0 <= r < 8 and 0 <= c < 8:
                    moves.append((r, c))
        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_queen_moves(row, col)
