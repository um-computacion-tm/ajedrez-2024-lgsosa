from ajedrez.pieces import Piece
from ajedrez.move_helper import MoveHelper

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♕", "♛", row, col)

    def get_possible_moves(self, board, row, col):
        diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        diagonal_moves = MoveHelper.generate_moves(diagonal_directions, row, col)

        straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        straight_moves = MoveHelper.generate_moves(straight_directions, row, col)

        return diagonal_moves + straight_moves
