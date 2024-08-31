from ajedrez.chess import Chess

def main():
    chess = Chess()
    while True:
        print(chess.show_board())  # Llama al método de instancia de Chess para mostrar el tablero
        
        # Verifica si alguno de los jugadores se quedó sin piezas
        if not chess.player1.pieces or not chess.player2.pieces:
            print(f"Game Over! {'Player 1' if not chess.player1.pieces else 'Player 2'} has no more pieces left.")
            break
        
        # Opción para terminar el juego de mutuo acuerdo
        end_game = input("Do you both agree to end the game? (yes/no): ").lower()
        if end_game == "yes":
            print("The game has ended by agreement.")
            break

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
