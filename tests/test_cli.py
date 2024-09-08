import unittest
from unittest.mock import patch, MagicMock
from ajedrez.chess import Chess
import os

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['\n'])  # Simula un "Enter"
    @patch('os.system')  # Simula el comando `os.system('clear')`
    def test_show_welcome_message(self, mock_os_system, mock_input):
        from main import show_welcome_message
        show_welcome_message()
        mock_os_system.assert_called_with('clear')  # Verifica que se llamó a 'clear'
        mock_input.assert_called()  # Verifica que se esperó a la entrada del usuario

    @patch('ajedrez.chess.Chess.show_board', return_value="Chess board")
    def test_game_starts_properly(self, mock_show_board):
        with patch('builtins.input', side_effect=['no', 'no', '1', '2', '1', '2']):  # Simula los inputs del jugador
            from main import main
            chess = Chess()
            main()
            self.assertTrue(mock_show_board.called)  # Verifica que se mostró el tablero

    @patch('builtins.input', side_effect=['yes', 'yes'])
    def test_game_ends_by_agreement(self, mock_input):
        from main import main
        chess = Chess()
        with patch('ajedrez.chess.Chess') as MockChess:
            mock_chess_instance = MockChess.return_value
            mock_chess_instance.__white_player__.__pieces__ = ['Piece1']  # Simula que tiene piezas
            mock_chess_instance.__black_player__.__pieces__ = ['Piece2']
            main()
            self.assertEqual(mock_input.call_count, 2)  # Se pidieron dos respuestas para finalizar el juego

    @patch('builtins.input', side_effect=['1', '2', '1', '2'])
    @patch('ajedrez.chess.Chess.move', MagicMock())
    def test_play_function_moves_pieces(self, mock_input):
        from main import play
        chess = Chess()
        play(chess)
        chess.move.assert_called_with(1, 2, 1, 2)  # Verifica que se movió la pieza correctamente

if __name__ == '__main__':
    unittest.main()
