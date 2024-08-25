import unittest
from ajedrez.board import Board
from ajedrez.chess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        #inicializa un nuevo tablero.
        self.board = Board()
        self.chess_game = Chess()

    def test_initial_turn(self):
        chess_game = Chess () #nueva partida
        self.assertEqual(chess_game.turn, "WHITE") #verifico que el 1er turno sea del blanco

    def test_turn_change_correctly(self):
        chess_game = Chess()  # Nueva partida
        self.assertEqual(chess_game.turn, "WHITE")  # Verifico que el primer turno sea del blanco

        # Realizo un movimiento (supongamos que es válido)
        chess_game.move(0, 0, 1, 0)  # (fila origen, columna origen, fila destino, columna destino)

        # Verifico el cambio de turno
        self.assertEqual(chess_game.turn, "BLACK")

    def test_turn_does_not_change_on_invalid_move(self):
        chess_game = Chess()
        chess_game.move(4, 4, 5, 5)  # Movimiento sin pieza en la posición de origen
        self.assertEqual(chess_game.turn, "WHITE")  # El turno no debería cambiar
        
if __name__ == "__main__":
    unittest.main()