import unittest
from unittest.mock import patch, MagicMock
from ajedrez.chess import Chess
from ajedrez.cli import Cli

class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        self.cli.chess = MagicMock(spec=Chess)
        self.cli.chess.white_player = MagicMock()
        self.cli.chess.black_player = MagicMock()
        self.cli.chess.white_player.pieces = ['pawn1', 'knight1']
        self.cli.chess.black_player.pieces = ['pawn2', 'knight2']
        self.cli.chess.get_board_state = MagicMock(return_value="Estado del tablero")


    @patch('builtins.input', side_effect=['start'])
    @patch('os.system') 
    def test_show_welcome_message(self, mock_clear, mock_input):
        self.cli.show_welcome_message()
        mock_clear.assert_called_once()
        self.assertTrue(mock_input.called)

    @patch('builtins.input', side_effect=['yes', 'yes'])
    def test_surrender_both_players_agree(self, mock_input):
        result = self.cli.surrender()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['yes', 'no'])
    def test_surrender_one_player_disagrees(self, mock_input):
        result = self.cli.surrender()
        self.assertFalse(result)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3'])
    def test_show_menu(self, mock_input, mock_print):
        result = self.cli.show_menu()
        self.assertEqual(result, '3')

    @patch('builtins.input', side_effect=['1', '1', '0', '1']) 
    def test_play_turn(self, mock_input):
        self.cli.chess.move.return_value = None
        self.cli.chess.white_player.pieces = ['pawn1']
        self.cli.chess.black_player.pieces = ['pawn2']

        result = self.cli.play()

        self.assertFalse(result)
        self.cli.chess.move.assert_called_once_with(1, 1, 0, 1)

    @patch('builtins.input', side_effect=['1', '0', '0', '1'])
    def test_play_turn_captures_king(self, mock_input):
        self.cli.chess.move.return_value = "WHITE"
        self.cli.chess.white_player.pieces = ['pawn1']
        self.cli.chess.black_player.pieces = ['king_black']

        result = self.cli.play()

        self.assertTrue(result)

    @patch('builtins.input', side_effect=['1', '1', '3', '0'])
    def test_play_turn_invalid_move(self, mock_input):
        self.cli.chess.move.side_effect = ValueError("Invalid move")
        result = self.cli.play()
        self.assertFalse(result)
        self.cli.chess.move.assert_called_once_with(1, 1, 3, 0)

    @patch('builtins.input', side_effect=['1', '0', '0', '0'])
    def test_play_turn_captures_king(self, mock_input):
        self.cli.chess.move.return_value = "WHITE"
        self.cli.chess.white_player.pieces = ['pawn1']
        self.cli.chess.black_player.pieces = ['king_black']
        
        result = self.cli.play()
        
        self.assertTrue(result)
        self.cli.chess.move.assert_called_once_with(1, 0, 0, 0)

    @patch('builtins.print')
    def test_show_board_state(self, mock_print):
        self.cli.show_board()
        self.cli.chess.get_board_state.assert_called_once()
        mock_print.assert_called_once_with("Estado del tablero")


if __name__ == '__main__':
    unittest.main()
