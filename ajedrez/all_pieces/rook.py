from ajedrez.pieces import Piece

class Rook(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♖", "♜", row, col)

    def get_possible_moves(self, board, row, col):
        return self.basic_rook_moves(row, col)

    def basic_rook_moves(self, row, col):
        moves = self.get_straight_moves(row, col)
        return moves

    def get_straight_moves(self, row, col):
        moves = []
        for r in range(8):
            if r != row:
                moves.append((r, col))

        for c in range(8):
            if c != col:
                moves.append((row, c))

        return moves
