from ajedrez.chess import Chess
from ajedrez.all_pieces.king import King
import os

class Cli:
    def __init__(self):
        self.chess = Chess()
    
    def show_welcome_message(self):
        os.system('clear')  # Clears the screen (on Linux/Mac)
        print("**********************************************")
        print("*                                            *")
        print("*                 CHESS                      *")
        print("*                                            *")
        print("**********************************************")
        print("\n Press Enter or any key to start...")
        input()  # Waits for the user to press any key

    def run(self):
        self.show_welcome_message()
        print("\n\n\nThe game has started...\n\n\n")
        game_active = True  # Juego sigue activo
        
        while game_active:
            print(self.chess.show_board())

            if self.chess.game_over(): 
                game_active = False 
                break

            choice = self.show_menu()

            if choice == "1":
                if self.play(): 
                    game_active = False
            elif choice == "2":
                if self.surrender():
                    game_active = False
                    return
            elif choice == "3":
                print("Game over. Exiting the game...")
                game_active = False
                return
            else:
                print("Invalid option. Please choose a valid option.")

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. Play a turn")
            print("2. Surrender")
            print("3. Exit the game")
            print("4. Show possible moves")
            
            choice = input("Choose an option (1, 2, 3, or 4): ")
            if choice in ['1', '2', '3', '4']:
                return choice
            else:
                print("Invalid option. Please choose a valid option.")


    def surrender(self):
        while True:
            player1_response = input("White Player, do you agree to surrender? (yes/no): ").lower()
            player2_response = input("Black Player, do you agree to surrender? (yes/no): ").lower()

            if player1_response == "yes" and player2_response == "yes":
                print("Both players agreed to surrender. The game has ended by surrender.")
                return True
            elif player1_response == "no" or player2_response == "no":
                print("One or both players chose not to surrender. The game will go on.")
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def play(self):
        try:
            print("Turn: ", self.chess.turn)
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
            to_row = int(input("To row: "))
            to_col = int(input("To col: "))

            # Mover la pieza en el tablero
            captured_king_color = self.chess.move(from_row, from_col, to_row, to_col)

            if captured_king_color:
                return True
            print(f"Current pieces count - White: {len(self.chess.__white_player__.__pieces__)}, Black: {len(self.chess.__black_player__.__pieces__)}")

        except Exception as e:
            print("Error: ", e)

        return False 

    def show_board(self):
        board_state = self.chess.get_board_state()  # Obtiene el estado del tablero
        print(board_state)

if __name__ == '__main__':
    cli = Cli()
    cli.run()
