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
        
        # Movimientos verticales
        moves.extend(self.generate_moves(row, col, direction="vertical"))
        
        # Movimientos horizontales
        moves.extend(self.generate_moves(row, col, direction="horizontal"))
        
        return moves

    def generate_moves(self, row, col, direction):
        moves = []
        if direction == "vertical":
            for r in range(8):
                if r != row:
                    moves.append((r, col))
        elif direction == "horizontal":
            for c in range(8):
                if c != col:
                    moves.append((row, c))
        return moves
