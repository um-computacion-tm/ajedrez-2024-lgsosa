import unittest
from ajedrez.all_pieces.rook import Rook
from ajedrez.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.white_rook = Rook("WHITE", 0, 0) 
        self.black_rook = Rook("BLACK", 7, 7)

    def test_rook_possible_moves(self):
        expected_moves_white_rook = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]
        possible_moves_white = self.white_rook.get_possible_moves(self.board, 0, 0)
        self.assertCountEqual(possible_moves_white, expected_moves_white_rook)

        expected_moves_black_rook = [
            (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), 
            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)
        ]
        possible_moves_black = self.black_rook.get_possible_moves(self.board, 7, 7)
        self.assertCountEqual(possible_moves_black, expected_moves_black_rook)

    def test_generate_moves_vertical(self):
        vertical_moves = self.white_rook.generate_moves(3, 3, direction="vertical")
        expected_vertical_moves = [(0, 3), (1, 3), (2, 3), (4, 3), (5, 3), (6, 3), (7, 3)]
        self.assertCountEqual(vertical_moves, expected_vertical_moves)

    def test_generate_moves_horizontal(self):
        horizontal_moves = self.white_rook.generate_moves(3, 3, direction="horizontal")
        expected_horizontal_moves = [(3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7)]
        self.assertCountEqual(horizontal_moves, expected_horizontal_moves)

if __name__ == '__main__':
    unittest.main()
