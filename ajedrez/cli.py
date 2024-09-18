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
    game_active = True  #juego sigue activo si o no? verifico con esto
    
    while game_active:
        print(chess.show_board())

        if game_over(chess):
            game_active = False
            break
        
        while True:
            player1_response = input("White Player, do you agree to end the game? (yes/no): ").lower()
            player2_response = input("Black Player, do you agree to end the game? (yes/no): ").lower()
            
            if player1_response == "yes" and player2_response == "yes":
                print("Both players agreed. The game has ended by agreement.")
                game_active = False
                return 
            elif player1_response == "no" or player2_response == "no":
                print("One or both players chose to continue. The game will go on.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        
        play(chess) 


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
    try:
        print("Turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col,
        )
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    main()
