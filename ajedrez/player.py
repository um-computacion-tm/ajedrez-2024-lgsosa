from ajedrez.board import Board

class Player():
    def __init__(self, color, board):
        self.__color__ = color 
        self.__board__ = board 
        self.__pieces__ = self._initialize_pieces_() 
        self.__captured_pieces__ = []


    def _initialize_pieces_(self):
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

    def add_captured_piece(self, piece):
        self.__captured_pieces__.append(piece)

    def remove_piece(self, piece):
        self.__pieces__.remove(piece)
    
    def get_color(self):
        return self.__color__
