from ajedrez.board import Board
from ajedrez.player import Player 

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__white_player__ = Player("WHITE", self.__board__)
        self.__black_player__ = Player("BLACK", self.__board__)
        self.__turn__ = "WHITE"

    def is_valid_move(self, piece, to_row, to_col):
        if piece.color != self.__turn__:
            print(f"Es el turno de {self.__turn__}. No puedes mover la pieza del oponente.")
            return False
        
        from_row = piece.row
        from_col = piece.col
        valid_moves = piece.get_possible_moves(self.__board__, from_row, from_col)
        if (to_row, to_col) not in valid_moves:
            return False
        if not self.__is_path_clear(piece, from_row, from_col, to_row, to_col):
            print("No puedes mover sobre otras piezas.")
            return False

        return True


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
            
        if not self.__white_player__.__pieces__:
            print("Black wins! White has no more pieces.")
            return
        elif not self.__black_player__.__pieces__:
            print("White wins! Black has no more pieces.")
            return

        self.__change_turn__()
    #para las piezas a mitad del camino q me faltaba
    def __is_path_clear(self, piece, from_row, from_col, to_row, to_col):
        delta_row = (to_row - from_row)
        delta_col = (to_col - from_col)

        step_row = 0
        step_col = 0

        if delta_row != 0:
            step_row = delta_row // abs(delta_row)  # -1 o 1
        if delta_col != 0:
            step_col = delta_col // abs(delta_col)  # -1 o 1

        current_row = from_row + step_row
        current_col = from_col + step_col

        while (current_row != to_row or current_col != to_col):
            if self.__board__.get_piece(current_row, current_col) is not None:
                return False  
            current_row += step_row
            current_col += step_col

        return True


    @property
    def turn(self):
        return self.__turn__

    def __change_turn__(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
        
    def show_board(self):
        return self.__board__.show_board()

    def game_over(self):
        return not self.__white_player__.__pieces__ or not self.__black_player__.__pieces__

    def get_current_player(self):
        return self.__white_player__ if self.__turn__ == "WHITE" else self.__black_player__
