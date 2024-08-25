from ajedrez.pieces import Piece

class Queen(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, row, col)

    def basic_queen_moves(self, row, col):
        moves = []
        
        # Definir las direcciones en las que se puede mover la reina
        directions = [
            (-1, -1), (-1, 1), (1, -1), (1, 1),  # Diagonales
            (-1, 0), (1, 0), (0, -1), (0, 1)    # Verticales y horizontales
        ]
        
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            
            # Continuar en esa dirección mientras estemos dentro del tablero
            while 0 <= r < 8 and 0 <= c < 8:
                moves.append((r, c))
                
                # Moverse más en la misma dirección (como la reina puede avanzar varias casillas)
                r += direction_r
                c += direction_c

        return moves
    
    def get_possible_moves(self, board, row, col):
        return self.basic_queen_moves(row, col)
