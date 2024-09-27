class Piece:
    def __init__(self, color, symbol_white, symbol_black, row=None, col=None):
        self._color = color
        self.row = row
        self.col = col
        self.symbol = symbol_white if color == "WHITE" else symbol_black  # Símbolo correcto según el color

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


