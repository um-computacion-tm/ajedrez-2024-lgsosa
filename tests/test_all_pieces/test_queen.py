import unittest
from ajedrez.all_pieces.queen import Queen

class TestQueen(unittest.TestCase):
    def test_basic_queen_moves(self):
        queen = Queen("black")  # Crea una reina

        start_row, start_col = 4, 4  # Coordenadas iniciales válidas
        expected_moves = []

        # Diagonal arriba I
        r, c = start_row - 1, start_col - 1
        while r >= 0 and c >= 0:  # En el tablero (coordenadas max I)
            expected_moves.append((r, c))
            r -= 1
            c -= 1

        # Diagonal arriba D
        r, c = start_row - 1, start_col + 1
        while r >= 0 and c <= 7:  # En el tablero (coordenadas max D)
            expected_moves.append((r, c))
            r -= 1
            c += 1

        # Diagonal abajo I
        r, c = start_row + 1, start_col - 1
        while r <= 7 and c >= 0:  # En el tablero
            expected_moves.append((r, c))
            r += 1
            c -= 1

        # Diagonal abajo D
        r, c = start_row + 1, start_col + 1
        while r <= 7 and c <= 7:  # En el tablero
            expected_moves.append((r, c))
            r += 1
            c += 1

        # Movimientos verticales (arriba y abajo)
        for r in range(8):
            if r != start_row:
                expected_moves.append((r, start_col))

        # Movimientos horizontales (izquierda y derecha)
        for c in range(8):
            if c != start_col:
                expected_moves.append((start_row, c))

        # Compara los movimientos esperados con los movimientos generados
        self.assertEqual(set(queen.basic_queen_moves(start_row, start_col)), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
