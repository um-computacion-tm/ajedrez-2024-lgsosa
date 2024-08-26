from ajedrez.board import Board
from ajedrez.pieces import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    

    def is_valid_move(self, piece, to_row, to_col):
        if not isinstance(piece, Piece):
            print("Error: piece is not a valid instance of Piece.")
            return False
        valid_moves = piece.get_possible_moves(self.__board__, piece.row, piece.col)
        print(f"Valid moves for {piece}: {valid_moves}")  # Depuración
        return (to_row, to_col) in valid_moves


    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is not None and self.is_valid_move(piece, to_row, to_col):
            self.__board__.remove_piece(from_row, from_col)
            piece.set_position(to_row, to_col)
            self.__board__.set_piece(piece, to_row, to_col)
            # Cambia el turno
            self.turn = "BLACK" if self.turn == "WHITE" else "WHITE"
            print(f"Turno cambiado a: {self.turn}")  # Línea de depuración
        else:
            print("Movimiento inválido.")


    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
