from ajedrez.pieces import Piece, Directions

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♘", "♞", row, col)

    def basic_knight_moves(self, row, col):
        moves = []
        possible_moves = Directions.knight_moves()  # Usar los movimientos del caballo

        for direction_r, direction_c in possible_moves:
            r, c = row + direction_r, col + direction_c
            if 0 <= r < 8 and 0 <= c < 8:
                moves.append((r, c))

        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_knight_moves(row, col)
