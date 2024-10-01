from ajedrez.pieces import Piece

class Alfils(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row=row, col=col)
        self.symbol = "♗" if color == "WHITE" else "♝"

    def diagonal_moves(row, col, delta_row, delta_col):  #cambie todo en uno y calculo los movimientos por un lado
        movimientos = []
        r, c = row + delta_row, col + delta_col
        while 0 <= r <= 7 and 0 <= c <= 7:
            movimientos.append((r, c))
            r += delta_row
            c += delta_col
        return movimientos
    
    def basic_alfils_moves(self, row, col): #(+mantenimiento)
        moves = []
        
        moves += Alfils.diagonal_moves(row, col, -1, -1)
        moves += Alfils.diagonal_moves(row, col, -1, 1)
        moves += Alfils.diagonal_moves(row, col, 1, -1)
        moves += Alfils.diagonal_moves(row, col, 1, 1)
        return moves
    
    def get_possible_moves(self, board, row, col ):
        return self.basic_alfils_moves(row,col)

#############