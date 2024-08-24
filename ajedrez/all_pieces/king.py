from ajedrez.pieces import Piece

class King(Piece):
    def basic_king_moves(self,row,col):
        moves=[]

        directions = [
            (3, 3)  (3, 4)  (3, 5)
            (4, 3)  (4, 4)  (4, 5)
            (5, 3)  (5, 4)  (5, 5)
]
        
        #itero sobre todas las direcciones
        for direction_row, direction_col in directions:
            r , c  = row + direction_row, col + direction_col

            # Verifico si la nueva posición está dentro del tablero
            if 0 <= r <= 7 and 0 <= c <= 7:
                moves.append((r,c))
                
        return moves