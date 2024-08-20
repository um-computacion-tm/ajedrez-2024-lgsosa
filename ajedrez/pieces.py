class Piece:  # Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

### TORRES ###
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

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
#############

class Alfils(Piece):
    def movimientos_basicos_de_alfiles(self, row, col):
        moves = []

        ### ARRIBA IZQUIERDA ###
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            moves.append((r, c))
            r -= 1
            c -= 1

        ### ARRIBA DERECHA ###
        r, c = row - 1, col + 1
        while r >= 0 and c <= 7:
            moves.append((r, c))
            r -= 1
            c += 1

        ### ABAJO IZQUIERDA ###
        r, c = row + 1, col - 1
        while r <= 7 and c >= 0:
            moves.append((r, c))
            r += 1
            c -= 1

        ### ABAJO DERECHA ###
        r, c = row + 1, col + 1
        while r <= 7 and c <= 7:
            moves.append((r, c))
            r += 1
            c += 1

        return moves
#############

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def basic_knight_moves(self, row, col):
        moves = []
        possible_moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]
    
        for direction_r , direction_c in possible_moves:
            r , c = row + direction_r, col + direction_c
            if 0<= r < 8 and 0 <= c <=8: #in the board
                moves.append((r,c))
            
        return moves

#############

### REINAS ###
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

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


#############

### PEONES ###
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def basic_pawn_moves(self, row, col):
        moves = []

        possibles_direction = []

        if self.color == "WHITE": #modificar y dejarlo con coordenadas (vectores)

            return [(0, 1), (0, 2), (-1, 1), (1, 1)]
        
        elif self.color == 'BLACK':

            return [(0, -1), (0, -2), (-1, -1), (1, -1)]


    def eat_pieces_with_peon(self, row, col):
            moves = []

            if self.color == "WHITE":

                r, c = row - 1, col - 1
                while r >= 0 and c >= 0:
                    moves.append((r, c))
                    r -= 1
                    c -= 1

                r, c = row - 1, col + 1
                while r >= 0 and c <= 7:
                    moves.append((r, c))
                    r -= 1
                    c += 1
            
            elif self.color == "BLACK":

                r, c = row + 1, col - 1
                while r <= 7 and c >= 0:
                    moves.append((r, c))
                    r += 1
                    c -= 1

                r, c = row + 1, col + 1
                while r <= 7 and c <= 7:
                    moves.append((r, c))
                    r += 1
                    c += 1
                
            return moves

#in test_eat_pieces_with_pawn_black
#    self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(moves))
#TypeError: 'NoneType' object is not iterable  
# ESTE ERROR  FUE PORQUE OLVIDE UN "RETURN"


#############
