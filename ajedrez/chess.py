from ajedrez.board import Board
from ajedrez.pieces import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__pieces__ = Piece(color="WHITE")

    def is_valid_move(self, piece, to_row, to_col):
        from_row = piece.row
        from_col = piece.col
        valid_moves = piece.get_possible_moves(self.__board__, from_row, from_col)
        return (to_row, to_col) in valid_moves



    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise ValueError("No piece at the given position")
        
        if not self.is_valid_move(piece, to_row, to_col):
            raise ValueError("Invalid move")

        # Mueve la pieza al nuevo destino
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        
        # Cambia el turno
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"

    @property
    def turn(self):
        return self.__turn__

    def __change_turn__(self):
        self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
