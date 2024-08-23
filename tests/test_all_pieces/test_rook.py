import unittest
from ajedrez.all_pieces.rook import Rook

class TestRook(unittest.TestCase):
    def test_movimientos_basicos_de_torres(self):
        rook = Rook("blanco")
        self.assertEqual(rook.color, "blanco")
        expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
        self.assertEqual(rook.movimientos_basicos_de_torres(0, 0), expected_moves)

        
if __name__ == '__main__':
    unittest.main()

