import unittest
from ajedrez.all_pieces.pawn import Pawn
from ajedrez.board import Board  # Asegúrate de que Board esté correctamente importado

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        # Inicializa los peones blancos y negros
        self.pawn_white = Pawn("WHITE", 6, 1)
        self.pawn_black = Pawn("BLACK", 1, 1)
        self.board = Board()  # Asume que Board es la clase que define el tablero
    
    def test_basic_pawn_moves_white(self):
        expected_moves = [(5, 1), (4, 1)]
        self.assertEqual(self.pawn_white.basic_pawn_moves(6, 1), expected_moves)
    
    def test_basic_pawn_moves_black(self):
        expected_moves = [(2, 1), (3, 1)]
        self.assertEqual(self.pawn_black.basic_pawn_moves(1, 1), expected_moves)
    
    def test_eat_pieces_with_peon_white(self):
        expected_moves = [(5, 0), (5, 2)]
        self.assertEqual(self.pawn_white.eat_pieces_with_peon(6, 1), expected_moves)
    
    def test_eat_pieces_with_peon_black(self):
        expected_moves = [(2, 0), (2, 2)]
        self.assertEqual(self.pawn_black.eat_pieces_with_peon(1, 1), expected_moves)
    
    def test_get_possible_moves_white(self):
        expected_moves = [(5, 1), (4, 1), (5, 0), (5, 2)]
        self.assertEqual(self.pawn_white.get_possible_moves(self.board, 6, 1), expected_moves)
    
    def test_get_possible_moves_black(self):
        expected_moves = [(2, 1), (3, 1), (2, 0), (2, 2)]
        self.assertEqual(self.pawn_black.get_possible_moves(self.board, 1, 1), expected_moves)

if __name__ == '__main__':
    unittest.main()
