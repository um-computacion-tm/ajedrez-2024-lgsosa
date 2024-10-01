from ajedrez.pieces import Piece

class Pawn(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♙", "♟", row, col)
        
    def basic_pawn_moves(self, row, col):
        moves = []
        if self.color == "WHITE":
            if row > 0:
                moves.append((row - 1, col))  # Movimiento hacia adelante
                if row == 6:
                    moves.append((row - 2, col))  # Movimiento inicial doble
        elif self.color == "BLACK":
            if row < 7:
                moves.append((row + 1, col))  # Movimiento hacia adelante
                if row == 1:
                    moves.append((row + 2, col))  # Movimiento inicial doble
        return moves

    @staticmethod
    def diagonal_moves(row, col, delta_row, delta_col):
        movimientos = []
        r, c = row + delta_row, col + delta_col
        if 0 <= r <= 7 and 0 <= c <= 7:
            movimientos.append((r, c))
        return movimientos

    def eat_pieces_with_peon(self, row, col):
        movimientos = []
        directions = [(-1, -1), (-1, 1)] if self.color == "WHITE" else [(1, -1), (1, 1)]
        
        for dx, dy in directions:
            movimientos += Pawn.diagonal_moves(row, col, dx, dy)
        
        return movimientos

    def get_possible_moves(self, board, row, col):
        moves = self.basic_pawn_moves(row, col)
        moves += self.eat_pieces_with_peon(row, col)
        return moves