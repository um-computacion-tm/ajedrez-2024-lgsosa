from ajedrez.pieces import Piece, PieceMover

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♘", "♞", row, col)

    def get_possible_moves(self, board, row, col):
        directions = PieceMover.get_directions('knight_moves')
        return PieceMover.generate_moves(row, col, directions, board, max_steps=1)  # Caballo solo se mueve 1 paso
