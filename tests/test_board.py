import unittest
from ajedrez.all_pieces.rook import Rook
from ajedrez.all_pieces.knight import Knight
from ajedrez.all_pieces.alfils import Alfils
from ajedrez.all_pieces.queen import Queen
from ajedrez.all_pieces.king import King
from ajedrez.all_pieces.pawn import Pawn
from ajedrez.board import Board

class TestChessBoard(unittest.TestCase):
    
    def setUp(self):
        self.board = Board() 

    def test_initial_pieces(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(7, 4), King)
    
    def test_pawn_rows(self):
        for i in range(8):
            self.assertIsInstance(self.board.get_piece(1, i), Pawn)
            self.assertIsInstance(self.board.get_piece(6, i), Pawn)
    
    def test_is_empty(self):
        self.assertTrue(self.board.is_empty(4, 4))  # Debería estar vacío
        self.assertFalse(self.board.is_empty(0, 0))  # Debería haber una torre
    
    def test_move_piece(self):
        self.board.move_piece(1, 0, 2, 0) 
        self.assertIsInstance(self.board.get_piece(2, 0), Pawn)  
        self.assertTrue(self.board.is_empty(1, 0))

    def test_invalid_move_out_of_bounds(self):
        with self.assertRaises(ValueError):
            self.board.move_piece(0, 0, -1, 0)  # Fuera de los límites
    
    def test_invalid_move_same_color(self):
        with self.assertRaises(ValueError):
            self.board.move_piece(7, 0, 7, 1)  # Movimiento inválido (piezas del mismo color)
    
    def test_remove_piece(self):
        self.board.remove_piece(0, 0) 
        self.assertTrue(self.board.is_empty(0, 0)) 
    
    def test_show_board(self):
        board_str = self.board.show_board()
        self.assertIsInstance(board_str, str)
        self.assertIn("♖", board_str)
        self.assertIn("♟", board_str)

    def test_board_after_multiple_moves(self):
        self.board.move_piece(1, 0, 3, 0) 
        self.board.move_piece(6, 0, 4, 0)
        self.assertIsInstance(self.board.get_piece(3, 0), Pawn) 
        self.assertIsInstance(self.board.get_piece(4, 0), Pawn) 

    def test_move_piece_capture(self):
        self.board.move_piece(1, 0, 2, 0) 
        
        self.board.set_piece(Knight("WHITE", 2, 0), 2, 0) 
        
        self.board.move_piece(2, 0, 3, 0) 
        self.assertIsInstance(self.board.get_piece(3, 0), Knight) 
        self.assertTrue(self.board.is_empty(2, 0)) 


if __name__ == '__main__':
    unittest.main()
