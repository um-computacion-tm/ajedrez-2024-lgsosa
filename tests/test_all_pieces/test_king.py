from ajedrez.all_pieces.king import King
import unittest

class TestKing(unittest.TestCase):

    def setUp(self):
        # Inicializa un rey blanco en una posición inicial
        self.king = King(color='white', row=4, col=4)

    def test_basic_king_moves_center(self):
        # Verifica los movimientos del rey cuando está en el centro del tablero
        expected_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        actual_moves = self.king.basic_king_moves(self.king.row, self.king.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_basic_king_moves_corner(self):
        # Verifica los movimientos del rey cuando está en una esquina del tablero
        self.king.row = 7
        self.king.col = 7
        expected_moves = [
            (6, 6), (6, 7), (7, 6)
        ]
        actual_moves = self.king.basic_king_moves(self.king.row, self.king.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_get_possible_moves(self):
        # Verifica que get_possible_moves llame correctamente a basic_king_moves
        expected_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        actual_moves = self.king.get_possible_moves(None, self.king.row, self.king.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
