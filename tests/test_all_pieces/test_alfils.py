import unittest
from ajedrez.all_pieces.alfils import Alfils

class TestAlfils(unittest.TestCase):
    def test_diagonal_moves(self):
        # Test para diagonal_moves
        expected_moves = [(2, 2), (1, 1), (0, 0)]  # Movimientos esperados para la diagonal superior izquierda desde (3, 3)
        self.assertEqual(Alfils.diagonal_moves(3, 3, -1, -1), expected_moves)

        expected_moves = [(2, 4), (1, 5), (0, 6)]  # Movimientos esperados para la diagonal superior derecha desde (3, 3)
        self.assertEqual(Alfils.diagonal_moves(3, 3, -1, 1), expected_moves)

        expected_moves = [(4, 2), (5, 1), (6, 0)]  # Movimientos esperados para la diagonal inferior izquierda desde (3, 3)
        self.assertEqual(Alfils.diagonal_moves(3, 3, 1, -1), expected_moves)

        expected_moves = [(4, 4), (5, 5), (6, 6), (7, 7)]  # Movimientos esperados para la diagonal inferior derecha desde (3, 3)
        self.assertEqual(Alfils.diagonal_moves(3, 3, 1, 1), expected_moves)

    def test_basic_alfils_moves(self):
        # Test para eat_pieces_with_peon
        alfils = Alfils("WHITE")
        expected_moves = [(2, 2), (1, 1), (0, 0), (2, 4), (1, 5), (0, 6), (4, 2), (5, 1), (6, 0), (4, 4), (5, 5), (6, 6), (7, 7)]
        self.assertEqual(alfils.basic_alfils_moves(3, 3), expected_moves)

if __name__ == '__main__':
    unittest.main()
