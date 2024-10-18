# Changelog
All notable changes to this project will be documented in this file.


# [0.0.41] - 2024-10-16
### Added
- Fixed final details (the game was repeating the winner message).
- The game is finalized.

# [0.0.40] - 2024-10-15
### Added
- Changes in Chess and Play (from Play in CLI, functions were being called incorrectly).
- Added properties in Chess.
- Updated Play in CLI.

# [0.0.39] - 2024-10-08
### Added
- Changes for Docker (there were issues with the code, Docker wasn't building the image correctly, so I had to fix it).

# [0.0.38] - 2024-10-06
### Added
- Changes in Chess because pieces could move over other pieces (changes in `is_valid_move`).
- Added `is_path_clear` in Chess.

# [0.0.37] - 2024-10-04
### Added
- Updated `Rook` movements.
- Updated `test_rook` to improve test coverage.

# [0.0.36] - 2024-10-03
### Added
- Refactored Rook movements for better maintainability.

# [0.0.35] - 2024-10-02
### Added
- Added a new game menu.

# [0.0.34] - 2024-10-01
### Added
- Updated `is_valid_move` in Chess.

# [0.0.33] - 2024-09-30
### Added
- Fixed color errors and re-added `self.symbols`.

# [0.0.32] - 2024-09-28
### Added
- Corrected color errors in Pawn, King, and Rook (updated `self.symbols`).

# [0.0.31] - 2024-09-27
### Added
- Changes to `all_pieces`, King, Pawn, and Rook (used `super().__init__(color, "♔", "♚", row, col)`).

# [0.0.30] - 2024-09-26
### Added
- Refactored `all_pieces` for better maintainability (used `super().__init__(color, "♔", "♚", row, col)`).

# [0.0.29] - 2024-09-23
### Added
- Updated `test_chess` for better test coverage.

# [0.0.28] - 2024-09-22
### Added
- Added `test_capture_piece` in `test_chess`.

# [0.0.27] - 2024-09-21
### Added
- Updated `test_player` and `Player`, removed `calculate_score` and its test.

# [0.0.26] - 2024-09-19
### Added
- Added additional tests in `Chess`.

# [0.0.25] - 2024-09-18
### Added
- Updated `CLI`, but final fix not implemented yet (the game doesn’t start).

# [0.0.24] - 2024-09-17
### Added
- Updated `CLI`.

# [0.0.23] - 2024-09-16
### Added
- Updated `Board`.
- Added `game_over` in `Chess`.

# [0.0.22] - 2024-09-14
### Added
- Added tests in `test_board` for better coverage (95%).

# [0.0.21] - 2024-09-11
### Added
- Added tests in `test_player`.

# [0.0.20] - 2024-09-08
### Added
- Updated `test_cli` and `test_pieces`.

# [0.0.19] - 2024-09-07
### Added
- Updated tests.

# [0.0.18] - 2024-09-06
### Added
- Added `show_welcome_message` in `Chess`.

# [0.0.17] - 2024-09-05
### Added
- Added `surrender` in `CLI`.

# [0.0.16] - 2024-09-04
### Added
- Updated `get_possible_moves` in `Alfils`.

# [0.0.15] - 2024-09-02
### Added
- Added `is_empty` in `Board`.

# [0.0.14] - 2024-09-01
### Added
- Added `def_main` in `CLI`.
- Updated `is_valid_move` in `Board`.

# [0.0.13] - 2024-08-31
### Added
- Updated all pieces and added `show_board` and more player options.

# [0.0.12] - 2024-08-30
### Added
- Added `Player` class.

# [0.0.11] - 2024-08-29
### Added
- Changes in Chess (fixed `self.turn`).
- Added `move_piece` in `Board`.
- Added tests in `test_chess`.

# [0.0.10] - 2024-08-28
### Added
- Fixed errors in `Pawn`.

# [0.0.9] - 2024-08-26
### Added
- Changes in Chess (added `basic_alfils_moves`).
- Added `get_piece`, `set_piece`, `remove_piece` in `Board`.

# [0.0.8] - 2024-08-25
### Added
- Added pieces to the board.

# [0.0.7] - 2024-08-24
### Added
- Added tests for King.

# [0.0.6] - 2024-08-23
### Added
- Added King.

# [0.0.5] - 2024-08-22
### Added
- Refactored folder structure.

# [0.0.4] - 2024-08-20
### Added
- Added Queen and its tests.
- Added Pawn and its tests.

# [0.0.3] - 2024-08-19
### Added
- Updated Board and its tests.
- Updated Knight, Chess, and CLI.
- Added tests.

# [0.0.2] - 2024-08-18
### Added
- Added Board and their tests.
- Added Knight.

# [0.0.1] - 2024-08-17
### Added
- Added pieces (Rook and Bishop), and their tests.
