from ajedrez.board import Board

class Jugador:
    def __init__(self,color):
        self.__color__ = color #ALMACENO el color del jugador
        self.__pieces__ = self._initialize_pieces_() #ALMACENO las piezas que movera cada jugador
        self.__board__= Board


    def _initialize_pieces_(self): #recorro del board y almaceno las piezas que pertenecen al jugador
        pieces = []
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece and piece.color == self.__color__:
                    pieces.append(piece)
        return pieces

    def move_piece(self, from_row, from_col, to_row, to_col): #
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise ValueError("No piece at the given position")
        
        if piece.color != self.__color__:
            raise ValueError("You cannot move the opponent's piece")
        
        self.__board__.move_piece(from_row, from_col, to_row, to_col)


    def add_piece(self, piece): #para agregar una pieza al jugador (si este consigue llegar con el peon al final del tablero)
        self.__pieces__.append(piece)

    def remove_piece(self, piece): #para eliminar la pieza del jugador (cdo esta sea comida)
        self.__pieces__.remove(piece)



#represento 1 jugador

#almaceno las piezas del jugador 

#metodo para mover y quitar piezas (si este las come)