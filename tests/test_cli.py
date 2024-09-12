import unittest
from unittest.mock import patch, MagicMock
from ajedrez.chess import Chess
from ajedrez.cli import main,show_welcome_message,play
import os

class TestChessGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['\n'])  # Simula un "Enter"
    @patch('os.system')  # Simula el comando `os.system('clear')`
    def test_show_welcome_message(self, mock_os_system, mock_input):
        show_welcome_message()
        mock_os_system.assert_called_with('clear')  # Verifica que se llamó a 'clear'
        mock_input.assert_called()  # Verifica que se esperó a la entrada del usuario


    @patch('builtins.input', side_effect=['1', '2', '1', '2'])
    @patch('ajedrez.chess.Chess.move', MagicMock())
    def test_play_function_moves_pieces(self, mock_input):
        chess = Chess()
        play(chess)
        chess.move.assert_called_with(1, 2, 1, 2)  # Verifica que se movió la pieza correctamente

if __name__ == '__main__':
    unittest.main()
