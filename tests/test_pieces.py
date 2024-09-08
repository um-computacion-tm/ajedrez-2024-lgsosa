import unittest
from ajedrez.pieces import Piece

class TestPiece(unittest.TestCase):

    def test_piece_initialization(self):
        piece = Piece('white', 0, 0)
        self.assertEqual(piece.color, 'white')  # Verifica que el color se asigna correctamente
        self.assertEqual(piece.row, 0)  # Verifica la fila inicial
        self.assertEqual(piece.col, 0)  # Verifica la columna inicial

    def test_piece_set_position(self):
        piece = Piece('black')
        piece.set_position(5, 3)
        self.assertEqual(piece.get_position(), (5, 3))  # Verifica que la posición se actualiza correctamente

    def test_get_position(self):
        piece = Piece('black', 7, 7)
        self.assertEqual(piece.get_position(), (7, 7))  # Verifica que devuelve la posición correcta

    def test_color_property(self):
        piece = Piece('white')
        self.assertEqual(piece.color, 'white')  # Verifica el getter de color

    def test_get_possible_moves(self):
        piece = Piece('black')
        self.assertIsNone(piece.get_possible_moves(None, 0, 0))  # Dado que no tiene implementación, debe devolver `None`

if __name__ == '__main__':
    unittest.main()
