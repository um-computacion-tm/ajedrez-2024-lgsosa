import unittest
from ajedrez.chess import Chess
from ajedrez.all_pieces.pawn import Pawn

class TestChess(unittest.TestCase):
    
    def setUp(self):
        """Este método se ejecuta antes de cada test para crear una nueva instancia del juego de ajedrez."""
        self.chess_game = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess_game.turn, "WHITE")

    def test_invalid_move(self):
        piece = self.chess_game.board.get_piece(1, 0)  # Suponiendo que esta es una posición de peón
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
            self.chess_game.move(3, 3, 4, 4)  # Mover desde una casilla vacía
        self.assertEqual(self.chess_game.turn, "WHITE")

    def test_game_over_white_wins(self):
        """Verifica que el juego termina correctamente cuando las piezas negras son capturadas."""
        self.chess_game.black_player.__pieces__ = []  # Elimina todas las piezas negras
        self.assertTrue(self.chess_game.game_over())

    def test_game_over_black_wins(self):
        """Verifica que el juego termina correctamente cuando las piezas blancas son capturadas."""
        self.chess_game.white_player.__pieces__ = []  # Elimina todas las piezas blancas
        self.assertTrue(self.chess_game.game_over())

    def test_valid_pawn_move(self):
        """Verifica que el peón blanco se mueva correctamente."""
        piece = self.chess_game.board.get_piece(6, 0)  # Peón en la posición inicial
        self.chess_game.move(6, 0, 5, 0)  # Mueve el peón hacia adelante
        self.assertEqual(self.chess_game.board.get_piece(5, 0), piece)

    def test_path_clear(self):
        """Verifica que el camino esté despejado para un movimiento válido."""
        self.chess_game.board.get_piece = lambda r, c: None  # Simulando que el camino está despejado
        piece = Pawn(color="WHITE", row=1, col=0)
        self.assertTrue(self.chess_game._Chess__is_path_clear(piece, 1, 0, 3, 0))  # Moviendo el peón hacia adelante

    def test_path_blocked(self):
        """Verifica que el camino esté bloqueado para un movimiento inválido."""
        blocking_piece = Pawn(color="BLACK", row=2, col=0)
        self.chess_game.board.get_piece = lambda r, c: blocking_piece if (r, c) == (2, 0) else None
        piece = Pawn(color="WHITE", row=1, col=0)
        self.assertFalse(self.chess_game._Chess__is_path_clear(piece, 1, 0, 3, 0))  # Camino bloqueado



if __name__ == '__main__':
    unittest.main()
