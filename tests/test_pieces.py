import unittest
from ajedrez.pieces import Rook, Alfils

class TestRook(unittest.TestCase):
    def test_movimientos_basicos_de_torres(self):
        rook = Rook("blanco")
        self.assertEqual(rook.color, "blanco")
        expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
        self.assertEqual(rook.movimientos_basicos_de_torres(0, 0), expected_moves)

class TestAlfils(unittest.TestCase):
    def test_movimientos_basicos_de_alfiles(self):
        alfils = Alfils("negro")
        self.assertEqual(alfils.color, "negro")
        expected_moves = [
            (i, j) for i in range(8) for j in range(8) if abs(i - 3) == abs(j - 3) and (i, j) != (3, 3)
        ]
        self.assertEqual(set(alfils.movimientos_basicos_de_alfiles(3, 3)), set(expected_moves))

if __name__ == '__main__':
    unittest.main()

