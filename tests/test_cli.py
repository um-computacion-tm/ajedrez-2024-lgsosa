import unittest
from unittest.mock import patch, MagicMock
from ajedrez.chess import Chess
from ajedrez.cli import show_welcome_message, show_menu, surrender, game_over, play

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['\n'])
    @patch('os.system')
    def test_show_welcome_message(self, mock_os_system, mock_input):
        # Testea que se muestra el mensaje de bienvenida y se limpia la pantalla
        show_welcome_message()
        mock_os_system.assert_called_with('clear')
        mock_input.assert_called()

    @patch('builtins.input', side_effect=['1'])
    def test_show_menu(self, mock_input):
        # Testea que la opción de jugar se selecciona correctamente
        result = show_menu()
        self.assertEqual(result, '1')

    @patch('builtins.input', side_effect=['yes', 'yes'])
    def test_surrender_both_agree(self, mock_input):
        # Testea que ambos jugadores aceptan rendirse
        chess = Chess()
        result = surrender(chess)
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['yes', 'no'])
    def test_surrender_one_disagrees(self, mock_input):
        # Testea que uno de los jugadores no acepta rendirse
        chess = Chess()
        result = surrender(chess)
        self.assertFalse(result)

    def test_game_over_white_king_captured(self):
        # Testea cuando el rey blanco es capturado
        chess = Chess()
        with patch.object(chess, '__white_player__', MagicMock(__pieces__=[])):
            result = game_over(chess)
            self.assertTrue(result)

    def test_game_over_black_king_captured(self):
        # Testea cuando el rey negro es capturado
        chess = Chess()
        with patch.object(chess, '__black_player__', MagicMock(__pieces__=[])):
            result = game_over(chess)
            self.assertTrue(result)

    @patch('builtins.input', side_effect=['1', '1', '2', '2'])
    def test_play(self, mock_input):
        # Testea el flujo de juego básico
        chess = Chess()
        with patch.object(chess, 'move') as mock_move:
            play(chess)
            mock_move.assert_called_with(1, 1, 2, 2)

if __name__ == '__main__':
    unittest.main()
