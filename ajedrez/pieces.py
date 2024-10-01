class Piece():
    def __init__(self, color, symbol=None, row=None, col=None):
        self._color = color
        self.symbol = symbol
        self.row = row
        self.col = col


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


