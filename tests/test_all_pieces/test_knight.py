import unittest
from ajedrez.all_pieces.knight import Knight
from ajedrez.board import Board  

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.knight_white = Knight("white", 4, 4)
        self.knight_black = Knight("black", 0, 0)

    def test_knight_moves_center(self):

        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        possible_moves = self.knight_white.get_possible_moves(self.board, 4, 4)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_knight_moves_corner(self):

        expected_moves = [
            (2, 1), (1, 2)
        ]
        possible_moves = self.knight_black.get_possible_moves(self.board, 0, 0)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_knight_moves_edge(self):
        knight_edge = Knight("white", 0, 4)
        expected_moves = [
            (2, 3), (2, 5), (1, 2), (1, 6)
        ]
        possible_moves = knight_edge.get_possible_moves(self.board, 0, 4)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_knight_moves_out_of_bounds(self):
        knight_edge = Knight("white", 7, 7) 
        expected_moves = [
            (5, 6), (6, 5)
        ]
        possible_moves = knight_edge.get_possible_moves(self.board, 7, 7)
        self.assertEqual(set(possible_moves), set(expected_moves))

if __name__ == "__main__":
    unittest.main()
