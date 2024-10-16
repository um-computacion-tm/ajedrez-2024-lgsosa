import unittest
from ajedrez.all_pieces.alfils import Alfils

class TestAlfils(unittest.TestCase):

    def setUp(self):
        self.alfils = Alfils(color='white', row=4, col=4)

    def test_diagonal_moves(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  
            (3, 5), (2, 6), (1, 7),          
            (5, 3), (6, 2), (7, 1),         
            (5, 5), (6, 6), (7, 7)          
        ]

        actual_moves_left = Alfils.diagonal_moves(4, 4, -1, -1)
        actual_moves_right = Alfils.diagonal_moves(4, 4, -1, 1)
        actual_moves_down_left = Alfils.diagonal_moves(4, 4, 1, -1)
        actual_moves_down_right = Alfils.diagonal_moves(4, 4, 1, 1)

        actual_moves = (
            actual_moves_left +
            actual_moves_right +
            actual_moves_down_left +
            actual_moves_down_right
        )
        
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_basic_alfils_moves(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  
            (3, 5), (2, 6), (1, 7),         
            (5, 3), (6, 2), (7, 1),          
            (5, 5), (6, 6), (7, 7)           
        ]
        
        actual_moves = self.alfils.basic_alfils_moves(self.alfils.row, self.alfils.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_get_possible_moves(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  
            (3, 5), (2, 6), (1, 7),          
            (5, 3), (6, 2), (7, 1),          
            (5, 5), (6, 6), (7, 7)           
        ]
        
        actual_moves = self.alfils.get_possible_moves(None, self.alfils.row, self.alfils.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
