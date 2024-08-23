import unittest
from ajedrez.all_pieces.pawn import Pawn

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

