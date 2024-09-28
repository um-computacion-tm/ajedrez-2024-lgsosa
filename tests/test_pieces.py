import unittest
from ajedrez.pieces import Piece

class TestPiece(unittest.TestCase):

    def test_piece_initialization(self):
        # Verificar la inicialización de la pieza
        piece = Piece("WHITE", "♙", "♟", 0, 0)
        self.assertEqual(piece.color, "WHITE")
        self.assertEqual(piece.symbol, "♙")
        self.assertEqual(piece.row, 0)
        self.assertEqual(piece.col, 0)

        piece_black = Piece("BLACK", "♙", "♟", 7, 7)
        self.assertEqual(piece_black.color, "BLACK")
        self.assertEqual(piece_black.symbol, "♟")
        self.assertEqual(piece_black.row, 7)
        self.assertEqual(piece_black.col, 7)

    def test_color_property(self):
        # Verificar que la propiedad color funcione correctamente
        piece = Piece("WHITE", "♙", "♟")
        self.assertEqual(piece.color, "WHITE")

    def test_set_position(self):
        # Verificar que el método set_position funcione correctamente
        piece = Piece("WHITE", "♙", "♟", 0, 0)
        piece.set_position(3, 4)
        self.assertEqual(piece.get_position(), (3, 4))

    def test_get_position(self):
        # Verificar que el método get_position funcione correctamente
        piece = Piece("BLACK", "♟", "♙", 7, 7)
        self.assertEqual(piece.get_position(), (7, 7))

    def test_get_possible_moves(self):
        # Test para asegurar que el método get_possible_moves existe
        piece = Piece("WHITE", "♙", "♟")
        self.assertTrue(hasattr(piece, 'get_possible_moves'))
        self.assertEqual(piece.get_possible_moves(None, 0, 0), None)

if __name__ == '__main__':
    unittest.main()
