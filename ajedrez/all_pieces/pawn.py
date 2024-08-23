from ajedrez.pieces import Piece

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


    def diagonal_moves(row, col, delta_row, delta_col):  #cambie todo en uno y calculo los movimientos por un lado
        movimientos = []
        r, c = row + delta_row, col + delta_col
        while 0 <= r <= 7 and 0 <= c <= 7:
            movimientos.append((r, c))
            r += delta_row
            c += delta_col
        return movimientos

    def eat_pieces_with_peon(self, row, col): #la diagonal del peon ahora esta apartada y simplemente llama a la funcion diagonal_moves (+mantenimiento)
        movimientos = []
        if self.color == "WHITE":
            movimientos += Pawn.diagonal_moves(row, col, -1, -1)
            movimientos += Pawn.diagonal_moves(row, col, -1, 1)
        elif self.color == "BLACK":
            movimientos += Pawn.diagonal_moves(row, col, 1, -1)
            movimientos += Pawn.diagonal_moves(row, col, 1, 1)
        return movimientos

#in test_eat_pieces_with_pawn_black
#    self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(moves))
#TypeError: 'NoneType' object is not iterable  
# ESTE ERROR  FUE PORQUE OLVIDE UN "RETURN"