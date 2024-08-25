from ajedrez.board import Board
from ajedrez.pieces import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_valid_move(self, piece, to_row, to_col):
        valid_moves = piece.get_possible_moves(self.__board__, piece.row, piece.col)

        return (to_row, to_col) in valid_moves

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is not None and self.is_valid_move(piece, to_row, to_col):
            self.__board__.__positions__[to_row][to_col] = piece
            piece.set_position(to_row, to_col)  # Asegúrate de tener este método en la clase de la pieza
            self.__board__.__positions__[from_row][from_col] = None
            self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
