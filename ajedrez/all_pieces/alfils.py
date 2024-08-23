from ajedrez.pieces import Piece

class Alfils(Piece):
    def diagonal_moves(row, col, delta_row, delta_col):  #cambie todo en uno y calculo los movimientos por un lado
        movimientos = []
        r, c = row + delta_row, col + delta_col
        while 0 <= r <= 7 and 0 <= c <= 7:
            movimientos.append((r, c))
            r += delta_row
            c += delta_col
        return movimientos
    
    def eat_pieces_with_peon(self, row, col): #(+mantenimiento)
        moves = []
        
        moves += Alfils.diagonal_moves(row, col, -1, -1)
        moves += Alfils.diagonal_moves(row, col, -1, 1)
        moves += Alfils.diagonal_moves(row, col, 1, -1)
        moves += Alfils.diagonal_moves(row, col, 1, 1)
        return moves
#############