import unittest
from ajedrez.all_pieces.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        # Inicializa un caballo blanco en una posición inicial
        self.knight = Knight(color='white', row=4, col=4)

    def test_basic_knight_moves_center(self):
        # Verifica los movimientos del caballo cuando está en el centro del tablero
        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        actual_moves = self.knight.basic_knight_moves(self.knight.row, self.knight.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

    def test_basic_knight_moves_edge(self):
        # Verifica los movimientos del caballo cuando está en el borde del tablero
        self.knight.row = 0
        self.knight.col = 0
        expected_moves = [
            (1, 2), (2, 1)
        ]
        actual_moves = self.knight.basic_knight_moves(self.knight.row, self.knight.col)
        self.assertEqual(set(actual_moves), set(expected_moves))


    def test_get_possible_moves(self):
        # Verifica que get_possible_moves llame correctamente a basic_knight_moves
        expected_moves = [
            (2, 3), (2, 5), (3, 2), (3, 6),
            (5, 2), (5, 6), (6, 3), (6, 5)
        ]
        actual_moves = self.knight.get_possible_moves(None, self.knight.row, self.knight.col)
        self.assertEqual(set(actual_moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
