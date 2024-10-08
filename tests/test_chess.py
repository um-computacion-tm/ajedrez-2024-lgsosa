import unittest
from ajedrez.board import Board
from ajedrez.chess import Chess
from ajedrez.pieces import Piece


class TestChess(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada test para crear una nueva instancia del juego de ajedrez."""
        self.chess_game = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess_game.turn, "WHITE")

    def test_invalid_move(self):
        piece = self.chess_game.__board__.get_piece(1, 0)
        self.assertFalse(self.chess_game.is_valid_move(piece, 4, 0))

    def test_move_invalid(self):
        with self.assertRaises(ValueError):
            self.chess_game.move(1, 0, 4, 0)  # Intentar mover el peón blanco a una posición inválida


    def test_move_from_empty_square(self):
        """Verifica que intentar mover desde una casilla vacía levante un error."""
        with self.assertRaises(ValueError):
            self.chess_game.move(3, 3, 4, 4)  # Intentar mover desde una casilla vacía

    def test_turn_does_not_change_on_invalid_move(self):
        """Verifica que el turno no cambie cuando se realiza un movimiento inválido."""
        self.assertEqual(self.chess_game.turn, "WHITE")
        with self.assertRaises(ValueError):
            self.chess_game.move(3, 3, 4, 4)  # Mover desde una casilla vacía (movimiento inválido)
        self.assertEqual(self.chess_game.turn, "WHITE")  # El turno no debería haber cambiado

    def test_game_over_white_wins(self):
        """Verifica que el juego termina correctamente cuando las piezas negras son capturadas."""
        self.chess_game.__black_player__.__pieces__= []  # Elimina todas las piezas negras
        self.assertTrue(self.chess_game.game_over())  # El juego debería terminar


    def test_game_over_black_wins(self):
        """Verifica que el juego termina correctamente cuando las piezas blancas son capturadas."""
        self.chess_game.__white_player__.__pieces__= []  # Elimina todas las piezas blancas
        self.assertTrue(self.chess_game.game_over())

if __name__ == '__main__':
    unittest.main()
