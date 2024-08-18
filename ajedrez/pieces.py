class Piece:    #Clase Padre
    def __init__(self, color):
        self.__color__ = color

    @property             #Me toma como objeto privado el color entonces vi que si hago @property lo solucionaba
    
    def color(self):
        return self.__color__

###Tipo de Piezas###

###TORRES###
class Rook(Piece):     
    def __init__(self, color):
        super().__init__(color) 

    def movimientos_basicos_de_torres(self, row, col):

        moves = []

        # Muestra los Movimientos verticales (arriba y abajo) a los que poder mover tu torre
        for r in range(8):
            if r != row:
                moves.append((r, col))

        # Movimientos los horizontales (izquierda y derecha) a los que puede mover tu torre
        for c in range(8):
            if c != col:
                moves.append((row, c))

        return moves
#############

###ALFILS###
class Alfils(Piece):
    
    def movimientos_basicos_de_alfiles(self, row, col):
        
        moves = []

        #Voy a marcar las "row" como r para mayor comodidad y "col" como c

        ###ARRIBA IZQUIERDA###

        r, c = row -1, col -1 #Les resto 1 para hacer los movimentos arriba izquierda
        while r >=0 and c >=0:#Me permite hacer el movimiento las veces que quiera hasta que me salga del tablero en ese caso se corta el bucle
            moves.append((r, c)) #Los agrego
            r -= 1
            c -= 1

        ###ARRIBA DERECHA###

        r, c = row -1, col +1
        while r >=0 and c <=7:
            moves.append((r, c)) 
            r -= 1
            c += 1

        ###ABAJO IZQUIERDA###

        r, c = row +1, col -1
        while r <=7 and c >=0:
            moves.append((r, c)) 
            r += 1
            c -= 1

        ###ABAJO DERECHA###

        r, c = row +1, col +1
        while r <=7 and c <=7:
            moves.append((r, c)) 
            r += 1
            c += 1

        return moves
    
#############

###REYES###
class Knight(Piece):
    pass
#############

###REINAS###
class Queen(Piece):
    pass
#############

###CABALLOS###
class Horse(Piece):
    pass
#############

###PEONES###
class Pawn(Piece):     
    pass
#############