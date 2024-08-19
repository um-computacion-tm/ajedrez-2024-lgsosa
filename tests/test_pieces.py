import unittest
from ajedrez.pieces import Rook, Alfils, Knight

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


class TestKnight(unittest.TestCase):
    def test_basic_knight_moves(self):
        knight = Knight("blanco")
        self.assertEqual(knight.color, "blanco")

        # Coordenadas iniciales válidas
        start_row, start_col = 4, 4

        # Llamar a la función para obtener los movimientos calculados por la clase
        actual_moves = knight.basic_knight_moves(start_row, start_col)

        # Replicar la lógica de los posibles movimientos dentro del test
        expected_moves = []
        possible_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        
        for direction_r, direction_c in possible_moves:
            r, c = start_row + direction_r, start_col + direction_c
            if 0 <= r < 8 and 0 <= c < 8:
                expected_moves.append((r, c))

        # Comparar movimientos
        self.assertEqual(set(actual_moves), set(expected_moves))


if __name__ == '__main__':
    unittest.main()

