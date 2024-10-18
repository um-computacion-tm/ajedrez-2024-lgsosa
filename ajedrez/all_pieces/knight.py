from ajedrez.pieces import Piece

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♘", "♞", row, col)

    def basic_knight_moves(self):
        moves = []
        current_position = (self.row, self.col)

        # Lista de movimientos posibles del caballero
        possible_moves = [
            (current_position[0] - 2, current_position[1] - 1),
            (current_position[0] - 1, current_position[1] - 2),
            (current_position[0] + 1, current_position[1] - 2),
            (current_position[0] + 2, current_position[1] - 1),
            (current_position[0] + 2, current_position[1] + 1),
            (current_position[0] + 1, current_position[1] + 2),
            (current_position[0] - 1, current_position[1] + 2),
            (current_position[0] - 2, current_position[1] + 1),
        ]

        # Filtrar movimientos válidos dentro del tablero
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                moves.append(move)

        return moves

    def get_possible_moves(self, board, row, col):
        # Actualizar la posición de la pieza antes de calcular los movimientos
        self.row = row
        self.col = col
        
        # Obtener movimientos básicos sin restricción de otras piezas
        return self.basic_knight_moves()
