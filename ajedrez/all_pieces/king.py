from ajedrez.pieces import Piece
from ajedrez.move_helper import MoveHelper

class King(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♔", "♚", row, col)

    def get_possible_moves(self, board, row, col):
        moves = []
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if row_offset == 0 and col_offset == 0:
                    continue

                new_row = row + row_offset
                new_col = col + col_offset

                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    moves.append((new_row, new_col))

        return moves
