import unittest
from ajedrez.pieces import Rook, Alfils, Knight, Queen, Pawn

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

class TestPawn(unittest.TestCase):
    def test_basic_pawn_moves_black(self):
        pawn = Pawn("BLACK")#creo un peon
        self.assertEqual(pawn.color, "BLACK")
        expected_moves = [(0, -1), (0, -2), (-1, -1), (1, -1)]
        self.assertEqual(pawn.basic_pawn_moves(0, 0), expected_moves)

    def test_basic_pawn_moves_white(self):
        pawn = Pawn("WHITE")#creo un peon
        self.assertEqual(pawn.color, "WHITE")
        expected_moves = [(0, 1), (0, 2), (-1, 1), (1, 1)]
        self.assertEqual(pawn.basic_pawn_moves(0, 0), expected_moves)

    def test_eat_pieces_with_pawn_black(self):
        pawn = Pawn ("BLACK")
        self.assertEqual(pawn.color, "BLACK")
        moves = []
        start_row, start_col = 6, 1

        r, c = start_row + 1, start_col - 1
        while r <= 7 and c >= 0:
            moves.append((r, c))
            r += 1
            c -= 1

        r, c = start_row + 1, start_col + 1
        while r <= 7 and c <= 7:
            moves.append((r, c))
            r += 1
            c += 1


        self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(moves))

    def test_eat_pieces_with_pawn_white(self):
        pawn = Pawn ("WHITE")
        self.assertEqual(pawn.color, "WHITE")
        moves = []
        start_row, start_col = 6, 1

        r, c = start_row - 1, start_col - 1
        while r >= 0 and c >= 0:
                    moves.append((r, c))
                    r -= 1
                    c -= 1

        r, c = start_row - 1, start_col + 1
        while r >= 0 and c <= 7:
                    moves.append((r, c))
                    r -= 1
                    c += 1


        self.assertEqual(set(pawn.eat_pieces_with_peon(start_row, start_col)), set(moves))

if __name__ == '__main__':
    unittest.main()

