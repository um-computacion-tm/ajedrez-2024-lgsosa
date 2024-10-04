from ajedrez.pieces import Piece

class Rook(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♖", "♜", row, col)

    def get_possible_moves(self, board, row, col):
        return self.basic_rook_moves(row, col)

    def basic_rook_moves(self, row, col):
        return self.get_straight_moves(row, col)

    def get_straight_moves(self, row, col):
        moves = []

        moves.extend(self.generate_moves(row, col, range(8), axis="row"))
        moves.extend(self.generate_moves(row, col, range(8), axis="col"))
        
        return moves

    def generate_moves(self, row, col, range_vals, axis):
        moves = []
        for val in range_vals:
            if axis == "row" and val != row:
                moves.append((val, col))
            elif axis == "col" and val != col:
                moves.append((row, val))
        return moves
