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

class PieceMover:
    @staticmethod
    def get_directions(directions_type):
        directions_dict = {
            'diagonal': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            'straight': [(-1, 0), (1, 0), (0, -1), (0, 1)],
            'all_directions': [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
            'knight_moves': [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        }
        return directions_dict.get(directions_type, [])

    @staticmethod
    def generate_moves(row, col, directions, board, max_steps=float('inf')):
        moves = []
        for direction_r, direction_c in directions:
            r, c = row + direction_r, col + direction_c
            steps = 0
            while 0 <= r < 8 and 0 <= c < 8 and steps < max_steps:
                moves.append((r, c))
                r += direction_r
                c += direction_c
                steps += 1
        return moves
