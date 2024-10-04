from ajedrez.chess import Chess
import os

def show_welcome_message():
    os.system('clear') # Clears the screen (on Linux/Mac)
    print("**********************************************")
    print("*                                            *")
    print("*                 CHESS                      *")
    print("*                                            *")
    print("**********************************************")
    print("\n Press Enter or any key to start...")

    input() # Waits for the user to press any key

def main():
    show_welcome_message()
    print("\n\n\nThe game has started...\n\n\n")
    chess = Chess()
    game_active = True  # Juego sigue activo
    
    while game_active:
        print(chess.show_board())

        # Verifica si el juego ha terminado por captura de un rey
        if game_over(chess):
            game_active = False  # Termina el juego si se captura un rey
            break

        # Muestra el menú con opciones
        choice = show_menu()
        
        if choice == "1":
            # Turno del juego
            play(chess)
        elif choice == "2":
            # Intento de rendición
            if surrender(chess):
                game_active = False
                return  # Finaliza el juego
        elif choice == "3":
            # Salir del juego
            print("Game over. Exiting the game...")
            game_active = False
            return  # Finaliza el juego
        else:
            print("Invalid option. Please choose a valid option.")

def show_menu():
    """
    Muestra el menú con las opciones: Jugar, Rendirse, Salir.
    """
    print("\nMenu:")
    print("1. Play a turn")
    print("2. Surrender")
    print("3. Exit the game")
    return input("Choose an option (1, 2, or 3): ")

def surrender(chess):
    """
    Ambos jugadores deben estar de acuerdo para rendirse y finalizar el juego.
    """
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

def game_over(chess):
    """
    Verifica si el rey blanco o negro ha sido capturado usando el símbolo de cada rey.
    """
    white_king_alive = any(piece.symbol == "♔" for piece in chess.__white_player__.__pieces__)
    black_king_alive = any(piece.symbol == "♚" for piece in chess.__black_player__.__pieces__)
    
    if not white_king_alive:
        print("Game Over! Black Player wins. White's king has been captured.")
        return True
    elif not black_king_alive:
        print("Game Over! White Player wins. Black's king has been captured.")
        return True
    
    return False

def play(chess):
    """
    Lógica de un turno en el juego.
    """
    try:
        print("Turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        chess.move(from_row, from_col, to_row, to_col)
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    main()
