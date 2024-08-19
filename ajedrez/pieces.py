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
    pass
#############

### CABALLOS ###
class Horse(Piece):
    pass
#############

### PEONES ###
class Pawn(Piece):
    pass
#############

if __name__ == '__main__':
    rook = Rook('white')
    print("Movimientos básicos de la torre desde la posición (0, 0):")
    print(rook.movimientos_basicos_de_torres(0, 0))

    alfils = Alfils('black')
    print("\nMovimientos básicos de los alfiles desde la posición (3, 3):")
    print(alfils.movimientos_basicos_de_alfiles(3, 3))
