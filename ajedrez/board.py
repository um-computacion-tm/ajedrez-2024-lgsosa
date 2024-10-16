from ajedrez.all_pieces.rook import Rook
from ajedrez.all_pieces.knight import Knight
from ajedrez.all_pieces.alfils import Alfils
from ajedrez.all_pieces.queen import Queen
from ajedrez.all_pieces.king import King
from ajedrez.all_pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
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

    def is_empty(self, row, col):
        return self.get_piece(row, col) is None

    def set_piece(self, piece, row, col):
        self.__positions__[row][col] = piece
    
    def remove_piece(self, row, col):
        self.__positions__[row][col] = None
    
    def is_within_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def move_piece(self, from_row, from_col, to_row, to_col):
        # Verifica que el movimiento esté dentro de los límites del tablero
        if not self.is_within_bounds(to_row, to_col):
            raise ValueError("Move is out of bounds")
        
        # Obtén la pieza de la posición de origen
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("No piece at the given position")
        
        # Verifica si hay una pieza en la posición de destino
        destination_piece = self.get_piece(to_row, to_col)
        
        if destination_piece:
            if destination_piece.color == piece.color:
                # Si la pieza es del mismo color, es un movimiento inválido
                raise ValueError("You cannot move to a square occupied by your own piece")
            else:
                # Si la pieza es del color contrario, realizar captura
                if isinstance(destination_piece, King):
                    print(f"{piece.color} player wins! The opponent's King has been captured.")
                    self.game_over = True  # Marca el juego como terminado
                # Remover la pieza capturada
                self.remove_piece(to_row, to_col)
        
        # Actualiza la posición de la pieza
        piece.row = to_row
        piece.col = to_col
        
        # Coloca la pieza en la nueva posición
        self.set_piece(piece, to_row, to_col)
        
        # Elimina la pieza de la posición original
        self.remove_piece(from_row, from_col)

    def show_board(self):
        # Encabezado de columnas
        header = "   "  # Espacio inicial para la alineación
        header += " ".join([f"{i:^5}" for i in range(8)])  # Centrando los números
        board_str = header + "\n"

        for row_idx, row in enumerate(self.__positions__):
            row_str = f"{row_idx} "  # Número de fila
            for cell in row:
                if cell is None:
                    row_str += "[   ] "  # Espacio para las celdas vacías
                else:
                    row_str += f"[{cell.symbol:^3}] "  # Centrar símbolo de pieza
            board_str += row_str + "\n"

        return board_str
    
    def __getitem__(self, position):
        # Permite acceder a las casillas del tablero usando la sintaxis board[row][col]
        row, col = position
        return self.board[row][col]

    def __setitem__(self, position, piece):
        # Permite colocar piezas en el tablero usando la sintaxis board[row][col] = piece
        row, col = position
        self.board[row][col] = piece

    def display(self):
        # Método para mostrar el tablero
        for row in self.board:
            print([str(piece) if piece else " " for piece in row])