from ajedrez.all_pieces.king import King
import unittest

class TestKing(unittest.TestCase):
    def test_basic_kings_moves(self):
    
        king = King("BLACK")
        result = king.basic_king_moves(4,4) #le paso al metodo las coordenadas que quiero testear

        #lo que espero que haga
        expected_moves= [ 
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]

        self.assertEqual(set(result), set(expected_moves))


if __name__ == '__main__':
    unittest.main()