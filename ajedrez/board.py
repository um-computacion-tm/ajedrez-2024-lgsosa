from ajedrez.all_pieces.rook import Rook
from ajedrez.all_pieces.knight import Knight
from ajedrez.all_pieces.alfils import Alfils
from ajedrez.all_pieces.queen import Queen
from ajedrez.all_pieces.king import King
from ajedrez.all_pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for i in range(8):
            col = []
            for j in range(8):
                col.append(None)
            self.__positions__.append(col)
        
        # Torres
        self.__positions__[0][0] = Rook("BLACK", 0, 0)
        self.__positions__[0][7] = Rook("BLACK", 0, 7)
        self.__positions__[7][7] = Rook("WHITE", 7, 7)
        self.__positions__[7][0] = Rook("WHITE", 7, 0)

        # Caballos
        self.__positions__[0][1] = Knight("BLACK", 0, 1)
        self.__positions__[0][6] = Knight("BLACK", 0, 6)
        self.__positions__[7][1] = Knight("WHITE", 7, 1)
        self.__positions__[7][6] = Knight("WHITE", 7, 6)

        # Alfils
        self.__positions__[0][2] = Alfils("BLACK", 0, 2)
        self.__positions__[0][5] = Alfils("BLACK", 0, 5)
        self.__positions__[7][2] = Alfils("WHITE", 7, 2)
        self.__positions__[7][5] = Alfils("WHITE", 7, 5)

        # Reina y Rey
        self.__positions__[0][3] = Queen("BLACK", 0, 3)
        self.__positions__[0][4] = King("BLACK", 0, 4)
        self.__positions__[7][3] = Queen("WHITE", 7, 3)
        self.__positions__[7][4] = King("WHITE", 7, 4)

        # Peones
        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK", 1, i)
            self.__positions__[6][i] = Pawn("WHITE", 6, i)
        
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def set_piece(self, piece, row, col):
        self.__positions__[row][col] = piece
    
    def remove_piece(self, row, col):
        self.__positions__[row][col] = None
    
    def is_within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    