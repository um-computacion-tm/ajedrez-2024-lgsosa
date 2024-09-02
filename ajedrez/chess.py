from ajedrez.board import Board
from ajedrez.player import Player  # Asumiendo que ya tienes la clase Player
from ajedrez.pieces import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        #crear jugadores
        self.__white_player__ = Player("WHITE", self.__board__)
        self.__black_player__ = Player("BLACK", self.__board__)
        self.__turn__ = "WHITE"

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

        target_piece = self.__board__.get_piece(to_row, to_col)
        
        self.__board__.move_piece(from_row, from_col, to_row, to_col)

        if target_piece:
            current_player = self.__white_player__ if self.__turn__ == "WHITE" else self.__black_player__
            current_player.add_captured_piece(target_piece)

        self.__change_turn__()



    @property
    def turn(self):
        return self.__turn__

    def __change_turn__(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
        
    def show_board(self):
        return self.__board__.show_board()

    def game_over(self):
        return not self.__white_player__.pieces or not self.__black_player__.pieces

    def get_current_player(self):
        return self.__white_player__ if self.__turn__ == "WHITE" else self.__black_player__
