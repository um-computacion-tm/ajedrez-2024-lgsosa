from ajedrez.pieces import Piece, PieceMover

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♕", "♛", row, col)

    def get_possible_moves(self, board, row, col):
        directions = PieceMover.get_directions('diagonal') + PieceMover.get_directions('straight')
        return PieceMover.generate_moves(row, col, directions, board)
