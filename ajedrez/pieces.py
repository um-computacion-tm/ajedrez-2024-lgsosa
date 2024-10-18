class Piece():
    def __init__(self, color, symbol_white, symbol_black, row=None, col=None, board = None):
        self._color = color
        self.row = row
        self.col = col
        self.board = board
        self.symbol = self.assign_symbol(symbol_white, symbol_black)

    @property
    def color(self):
        return self._color

    def get_possible_moves(self, row, col):
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
