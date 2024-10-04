import unittest
from ajedrez.all_pieces.rook import Rook

class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook_white = Rook("WHITE", 0, 0)
        self.rook_black = Rook("BLACK", 7, 7)

    def test_straight_moves_from_corner(self):
        expected_moves = [(r, 0) for r in range(1, 8)] + [(0, c) for c in range(1, 8)]
        moves = self.rook_white.get_straight_moves(0, 0)
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_straight_moves_from_center(self):
        expected_moves = [(r, 3) for r in range(8) if r != 4] + [(4, c) for c in range(8) if c != 3]
        moves = self.rook_white.get_straight_moves(4, 3)
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_possible_moves_from_corner(self):
        expected_moves = [(r, 0) for r in range(1, 8)] + [(0, c) for c in range(1, 8)]
        moves = self.rook_white.get_possible_moves(None, 0, 0)
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_possible_moves_from_center(self):
        expected_moves = [(r, 4) for r in range(8) if r != 3] + [(3, c) for c in range(8) if c != 4]
        moves = self.rook_black.get_possible_moves(None, 3, 4)
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_symbol(self):
        self.assertEqual(self.rook_white.symbol, "♖")
        self.assertEqual(self.rook_black.symbol, "♜")

if __name__ == '__main__':
    unittest.main()
