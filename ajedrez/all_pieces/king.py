from ajedrez.pieces import Piece
from ajedrez.move_helper import MoveHelper

class King(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♔", "♚", row, col)

    def get_possible_moves(self, board, row, col):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),         ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]
        # El Rey solo puede moverse un paso a la vez
        return MoveHelper.generate_moves(directions, row, col, max_steps=1)

