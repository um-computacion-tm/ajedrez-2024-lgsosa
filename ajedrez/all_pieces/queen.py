from ajedrez.pieces import Piece
from ajedrez.move_helper import MoveHelper

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♕", "♛", row, col)

    def get_possible_moves(self, board, row, col):
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1),  # Diagonales
            (-1, 0), (1, 0), (0, -1), (0, 1)    # Verticales y horizontales
        ]
        return MoveHelper.generate_moves(directions, row, col)
