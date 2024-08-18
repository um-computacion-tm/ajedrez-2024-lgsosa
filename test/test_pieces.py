from ajedrez.pieces import Rook,Alfils, Piece


from typing import List, Tuple

class Test_Piece:
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class Test_Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def movimientos_basicos_de_torres(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []
        for r in range(8):
            if r != row:
                moves.append((r, col))
        for c in range(8):
            if c != col:
                moves.append((row, c))
        return moves

class Test_Alfils(Piece):
    def movimientos_basicos_de_alfiles(self, row: int, col: int) -> List[Tuple[int, int]]:
        moves = []
        r, c = row -1, col -1
        while r >=0 and c >=0:
            moves.append((r, c))
            r -= 1
            c -= 1
        r, c = row -1, col +1
        while r >=0 and c <=7:
            moves.append((r, c))
            r -= 1
            c += 1
        r, c = row +1, col -1
        while r <=7 and c >=0:
            moves.append((r, c))
            r += 1
            c -= 1
        r, c = row +1, col +1
        while r <=7 and c <=7:
            moves.append((r, c))
            r += 1
            c += 1
        return moves

def test_rook():
    r = Rook("blanco")
    assert r.color == "blanco", "Test Case Rook 1 Failed"
    expected_moves = [(i, 0) for i in range(8) if i != 0] + [(0, i) for i in range(8) if i != 0]
    assert r.movimientos_basicos_de_torres(0, 0) == expected_moves, "Test Case Rook 2 Failed"

def test_alfils():
    a = Alfils("negro")
    assert a.color == "negro", "Test Case Alfils 1 Failed"
    expected_moves = [
        (i, j) for i in range(8) for j in range(8) if abs(i - 3) == abs(j - 3) and (i, j) != (3, 3)
    ]
    assert set(a.movimientos_basicos_de_alfiles(3, 3)) == set(expected_moves), "Test Case Alfils 2 Failed"

if __name__ == '__main__':
    test_rook()
    test_alfils()
    print("Todos los test pasaron")
