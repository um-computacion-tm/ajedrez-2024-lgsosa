import unittest
from ajedrez.all_pieces.queen import Queen

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.queen = Queen(color='white', row=4, col=4)

    def test_basic_queen_moves_center(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0), 
            (3, 5), (2, 6), (1, 7),          
            (5, 3), (6, 2), (7, 1),          
            (5, 5), (6, 6), (7, 7),         
            (3, 4), (2, 4), (1, 4), (0, 4), 
            (5, 4), (6, 4), (7, 4),          
            (4, 3), (4, 2), (4, 1), (4, 0), 
            (4, 5), (4, 6), (4, 7)          
        ]
        
        actual_moves = self.queen.basic_queen_moves(self.queen.row, self.queen.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_get_possible_moves(self):
        expected_moves = [
            (3, 3), (2, 2), (1, 1), (0, 0),  
            (3, 5), (2, 6), (1, 7),          
            (5, 3), (6, 2), (7, 1),          
            (5, 5), (6, 6), (7, 7),         
            (3, 4), (2, 4), (1, 4), (0, 4),  
            (5, 4), (6, 4), (7, 4),          
            (4, 3), (4, 2), (4, 1), (4, 0),  
            (4, 5), (4, 6), (4, 7)          
        ]
        
        actual_moves = self.queen.get_possible_moves(None, self.queen.row, self.queen.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
