from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, row=None, col=None):
        self._color = color
        self.row = row
        self.col = col

    @property
    def color(self):
        return self._color
    
    @abstractmethod
    def get_possible_moves(self, board, row, col):
        pass

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_position(self):
        return self.row, self.col


