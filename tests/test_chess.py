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

        # Accedo al tablero desde la instancia de chess_game
        board = chess_game.__board__
        
        # Selecciono una pieza blanca válida (por ejemplo, un peón)
        piece = board.get_piece(6, 0)  # Obtengo el peón en (6, 0)
        
        # Realizo el movimiento (por ejemplo, el peón se mueve de (6, 0) a (5, 0))
        chess_game.move(6, 0, 5, 0)  # (fila origen, columna origen, fila destino, columna destino)

        # Verifico el cambio de turno
        self.assertEqual(chess_game.turn, "BLACK")


    def test_turn_does_not_change_on_invalid_move(self):
        chess_game = Chess()
        chess_game.move(4, 4, 5, 5)  # Movimiento sin pieza en la posición de origen
        self.assertEqual(chess_game.turn, "WHITE")  # El turno no debería cambiar
        
if __name__ == "__main__":
    unittest.main()