import unittest
from ajedrez.all_pieces.rook import Rook

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook = Rook(color="WHITE", row=0, col=0)

    def test_rook_moves_from_corner(self):
        expected_moves = [(i, 0) for i in range(1, 8)]
        expected_moves += [(0, j) for j in range(1, 8)]

        moves = self.rook.get_possible_moves(None, 0, 0)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_moves_from_center(self):
        self.rook.set_position(4, 4)
        expected_moves = [(i, 4) for i in range(8) if i != 4]
        expected_moves += [(4, j) for j in range(8) if j != 4]

        moves = self.rook.get_possible_moves(None, 4, 4)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_no_moves_outside_board(self):
        self.rook.set_position(7, 7)
        expected_moves = [(i, 7) for i in range(7)]
        expected_moves += [(7, j) for j in range(7)]

        moves = self.rook.get_possible_moves(None, 7, 7)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_moves_in_one_row(self):
        self.rook.set_position(3, 0)
        expected_moves = [(i, 0) for i in range(8) if i != 3]  
        expected_moves += [(3, j) for j in range(1, 8)] 

        moves = self.rook.get_possible_moves(None, 3, 0)
        self.assertCountEqual(moves, expected_moves)

    def test_rook_moves_in_one_column(self):
        self.rook.set_position(0, 3)
        expected_moves = [(i, 3) for i in range(1, 8)] 
        expected_moves += [(0, j) for j in range(8) if j != 3] 

        moves = self.rook.get_possible_moves(None, 0, 3)
        self.assertCountEqual(moves, expected_moves)

if __name__ == "__main__":
    unittest.main()
