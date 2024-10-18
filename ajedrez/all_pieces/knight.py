from ajedrez.pieces import Piece

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♘", "♞", row, col)

    def get_possible_moves(self, board, row, col):
        moves = [
            (row - 2, col - 1), (row - 1, col - 2), (row + 1, col - 2), (row + 2, col - 1),
            (row + 2, col + 1), (row + 1, col + 2), (row - 1, col + 2), (row - 2, col + 1)
        ]
        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]
