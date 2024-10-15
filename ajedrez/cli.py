from ajedrez.chess import Chess
import os

def show_welcome_message():
    os.system('clear')  # Clears the screen (on Linux/Mac)
    print("**********************************************")
    print("*                                            *")
    print("*                 CHESS                      *")
    print("*                                            *")
    print("**********************************************")
    print("\n Press Enter or any key to start...")
    input()  # Waits for the user to press any key

def main():
    show_welcome_message()
    print("\n\n\nThe game has started...\n\n\n")
    chess = Chess()
    game_active = True  # Juego sigue activo
    
    while game_active:
        print(chess.show_board())

        if game_over(chess):  # Verificar si el juego ha terminado
            game_active = False  # Cambiar estado del juego
            break  # Salir del bucle si el juego terminó

        choice = show_menu()

        if choice == "1":
            play(chess)
        elif choice == "2":
            if surrender(chess):
                game_active = False
                return
        elif choice == "3":
            print("Game over. Exiting the game...")
            game_active = False
            return
        else:
            print("Invalid option. Please choose a valid option.")

def show_menu():
    print("\nMenu:")
    print("1. Play a turn")
    print("2. Surrender")
    print("3. Exit the game")
    print("4. Show possible moves")
    return input("Choose an option (1, 2, 3, or 4): ")

def surrender(chess):
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

def play(chess):
    try:
        print("Turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))

        captured_piece = chess.move(from_row, from_col, to_row, to_col)
        
        if captured_piece:
            print(f"Capturing {captured_piece} at ({to_row}, {to_col})")
            if captured_piece.symbol in ["♔", "♚"]:
                print(f"{chess.turn} player wins! The opponent's King has been captured.")
            
            # Eliminar la pieza capturada de la lista de piezas del jugador correspondiente
            if captured_piece.color == 'white':
                chess.__white_player__.__pieces__.remove(captured_piece)
                print(f"Removed {captured_piece} from White's pieces. Remaining: {len(chess.__white_player__.__pieces__)}")
            else:
                chess.__black_player__.__pieces__.remove(captured_piece)
                print(f"Removed {captured_piece} from Black's pieces. Remaining: {len(chess.__black_player__.__pieces__)}")

        # Verificar cantidad de piezas después de cada jugada
        print(f"Current pieces count - White: {len(chess.__white_player__.__pieces__)}, Black: {len(chess.__black_player__.__pieces__)}")

    except Exception as e:
        print("Error: ", e)

def game_over(chess):
    # Depuración del estado de las piezas
    print(f"Checking game over: White pieces: {len(chess.__white_player__.__pieces__)}, Black pieces: {len(chess.__black_player__.__pieces__)}")
    
    white_king_alive = any(piece.symbol == "♔" for piece in chess.__white_player__.__pieces__)
    black_king_alive = any(piece.symbol == "♚" for piece in chess.__black_player__.__pieces__)

    # Depurar el estado del rey
    print(f"White King Alive: {white_king_alive}, Black King Alive: {black_king_alive}")
    
    if not white_king_alive:
        print("Game Over! Black Player wins. White's king has been captured.")
        return True

    if not black_king_alive:
        print("Game Over! White Player wins. Black's king has been captured.")
        return True

    return False  # El juego sigue

if __name__ == '__main__':
    main()
