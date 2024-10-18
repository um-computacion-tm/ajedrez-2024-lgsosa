import unittest
from ajedrez.all_pieces.queen import Queen
from ajedrez.board import Board  
from ajedrez.pieces import Piece

class TestQueen(unittest.TestCase):
    def setUp(self):
        # Inicializa un tablero para usar en los tests
        self.board = Board()
        self.queen_white = Queen("white", 4, 4)  # Reina blanca en el centro del tablero
        self.queen_black = Queen("black", 0, 0)  # Reina negra en la esquina superior izquierda

    def test_queen_moves_center(self):
        # Testea los movimientos de la reina blanca en el centro del tablero
        possible_moves = self.queen_white.get_possible_moves(self.board, 4, 4)
        
        # Movimientos diagonales y rectos desde el centro del tablero
        expected_moves = [
            # Movimientos diagonales
            (3, 3), (2, 2), (1, 1), (0, 0),
            (3, 5), (2, 6), (1, 7),
            (5, 3), (6, 2), (7, 1),
            (5, 5), (6, 6), (7, 7),

            # Movimientos verticales y horizontales
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7)
        ]

        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_queen_moves_corner(self):
        # Testea los movimientos de la reina negra en la esquina superior izquierda
        possible_moves = self.queen_black.get_possible_moves(self.board, 0, 0)
        
        expected_moves = [
            # Movimientos diagonales
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            # Movimientos verticales y horizontales
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
        ]

        self.assertEqual(set(possible_moves), set(expected_moves))

    def test_queen_moves_edge(self):
        # Testea los movimientos de la reina en el borde del tablero (fila 0, columna 4)
        queen_edge = Queen("white", 0, 4)
        possible_moves = queen_edge.get_possible_moves(self.board, 0, 4)

        expected_moves = [
            # Movimientos diagonales
            (1, 3), (2, 2), (3, 1), (4, 0),
            (1, 5), (2, 6), (3, 7),
            # Movimientos verticales y horizontales
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4),
            (0, 3), (0, 2), (0, 1), (0, 0),
            (0, 5), (0, 6), (0, 7)
        ]

        self.assertEqual(set(possible_moves), set(expected_moves))

if __name__ == "__main__":
    unittest.main()
