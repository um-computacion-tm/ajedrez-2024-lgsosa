import unittest
from ajedrez.all_pieces.king import King
from ajedrez.board import Board  # Asegúrate de que Board esté implementado
from ajedrez.move_helper import MoveHelper  # Asegúrate de que MoveHelper esté implementado

class TestKing(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Inicializa un tablero
        self.king_white = King("white", 4, 4)  # Crea un rey blanco en la posición (4, 4)
        self.king_black = King("black", 0, 0)  # Crea un rey negro en la posición (0, 0)

    def test_king_moves_center(self):
        # Testea los movimientos del rey blanco en el centro del tablero
        expected_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),           (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        possible_moves = self.king_white.get_possible_moves(self.board, 4, 4)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_king_moves_edge(self):
        # Testea los movimientos del rey negro en la esquina inferior izquierda
        expected_moves = [
            (0, 1), (1, 0), (1, 1)
        ]
        possible_moves = self.king_black.get_possible_moves(self.board, 0, 0)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_king_moves_corner(self):
        # Testea los movimientos del rey negro en la esquina superior derecha
        king_corner = King("black", 7, 7)  # Rey en la posición (7, 7)
        expected_moves = [
            (6, 6), (6, 7), (7, 6)
        ]
        possible_moves = king_corner.get_possible_moves(self.board, 7, 7)
        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_king_moves_within_board_limits(self):
        # Testea que el rey no se mueva fuera de los límites del tablero
        expected_moves = [
            (1, 1), (1, 0), (0, 1)
        ]
        possible_moves = self.king_black.get_possible_moves(self.board, 0, 0)
        self.assertEqual(set(possible_moves), set(expected_moves))

if __name__ == "__main__":
    unittest.main()
