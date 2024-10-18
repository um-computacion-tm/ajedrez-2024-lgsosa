class Piece():
    def __init__(self, color, symbol_white, symbol_black, row=None, col=None):
        self._color = color
        self.row = row
        self.col = col
        self.symbol = self.assign_symbol(symbol_white, symbol_black)

    @property
    def color(self):
        return self._color

    def get_possible_moves(self, board, row, col):
        pass

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col
    
    def assign_symbol(self, symbol_white, symbol_black):
        return symbol_white if self.color == "WHITE" else symbol_black
    
    def is_within_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

class Directions:
    @staticmethod
    def diagonal():
        return [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales
    
    @staticmethod
    def straight():
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Verticales y horizontales
    
    @staticmethod
    def all_directions():
        return [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # Todas direcciones

    @staticmethod
    def knight_moves():
        return [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
