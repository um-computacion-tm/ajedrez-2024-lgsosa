
import unittest
from ajedrez.all_pieces.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook = Rook(color='white', row=0, col=0)

    def test_get_possible_moves(self):
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, j) for j in range(1, 8)]
        actual_moves = self.rook.get_possible_moves(None, self.rook.row, self.rook.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_basic_rook_moves(self):
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, j) for j in range(1, 8)]
        actual_moves = self.rook.basic_rook_moves(self.rook.row, self.rook.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_get_straight_moves(self):
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, j) for j in range(1, 8)]
        actual_moves = self.rook.get_straight_moves(self.rook.row, self.rook.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_generate_moves_row(self):
        expected_moves = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        actual_moves = self.rook.generate_moves(0, 0, range(8), axis="row")
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_generate_moves_col(self):
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        actual_moves = self.rook.generate_moves(0, 0, range(8), axis="col")
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
