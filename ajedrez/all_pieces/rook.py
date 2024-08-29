from ajedrez.pieces import Piece

### TORRES ###
class Rook(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, row, col)
        
    def movimientos_basicos_de_torres(self, row, col):
        moves = []

        # Movimientos verticales (arriba y abajo)
        for r in range(8):
            if r != row:
                moves.append((r, col))

        # Movimientos horizontales (izquierda y derecha)
        for c in range(8):
            if c != col:
                moves.append((row, c))

        return moves

    def get_possible_moves(self, board, row, col):
        return self.movimientos_basicos_de_torres(row, col)
#############