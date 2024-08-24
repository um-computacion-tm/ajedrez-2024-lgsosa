from ajedrez.pieces import Piece

class King(Piece):
    def basic_king_moves(self,row,col):
        moves=[]

        #coordenadas relativas
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),         ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        
        #itero sobre todas las direcciones
        for direction_row, direction_col in directions:
            r , c  = row + direction_row, col + direction_col

            # Verifico si la nueva posición está dentro del tablero
            if 0 <= r <= 7 and 0 <= c <= 7:
                moves.append((r,c))
                
        return moves