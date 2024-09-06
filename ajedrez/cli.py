from ajedrez.chess import Chess
import os

def show_welcome_message():
    os.system('clear') # Clears the screen (on Linux/Mac)
    print("**********************************************")
    print("* *")
    print("* CHESS *")
    print("* *")
    print("**********************************************")
    print("\n Press Enter or any key to start...")

    input() # Waits for the user to press any key

def main():
    show_welcome_message()
    print("\n\n\nThe game has started...\n\n\n")
    chess = Chess()
    while True:
        print(chess.show_board())
        
        # Verifica si alguno de los jugadores se quedó sin piezas
        if not chess.__white_player__.__pieces__ or not chess.__black_player__.__pieces__:
            print(f"Game Over! {'White Player' if not chess.__white_player__.__pieces__ else 'Black Player'} has no more pieces left.")
            break
        
        # Opción para terminar el juego de mutuo acuerdo
        while True:
            player1_response = input("White Player, do you agree to end the game? (yes/no): ").lower()
            player2_response = input("Black Player, do you agree to end the game? (yes/no): ").lower()
            
            # Ambos deben ingresar 'yes' para finalizar
            if player1_response == "yes" and player2_response == "yes":
                print("Both players agreed. The game has ended by agreement.")
                return  # Termina el juego
            elif player1_response == "no" or player2_response == "no":
                print("One or both players chose to continue. The game will go on.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        play(chess)
        
def play(chess):
    try:
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
    except Exception as e:
        print("error", e)

if __name__ == '__main__':
    main()
