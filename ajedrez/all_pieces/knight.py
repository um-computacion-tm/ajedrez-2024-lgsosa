from ajedrez.pieces import Piece

class Knight(Piece):
    def __init__(self, color, row=None, col=None):
        super().__init__(color, "♞", "♘", row, col)

    def move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            destination_piece = board[end_row][end_col]
            return destination_piece is None or destination_piece.color != self.color

        return False
