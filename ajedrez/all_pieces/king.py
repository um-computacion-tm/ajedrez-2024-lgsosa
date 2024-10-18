from ajedrez.pieces import Piece, PieceMover

class King(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♔", "♚", row, col)

    def get_possible_moves(self, board, row, col):
        directions = PieceMover.get_directions('all_directions')
        return PieceMover.generate_moves(row, col, directions, board, max_steps=1)  # Solo puede moverse 1 casilla
