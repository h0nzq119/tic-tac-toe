# Funkce pro vykreslení herní tabulky
def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        print("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
        print("+---+---+---+")

# Funkce pro kontrolu výhry
def check_winner(board, player):
    # Kontrola horizontál
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] == player:
            return True
    # Kontrola vertikál
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Kontrola diagonál
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Funkce pro kontrolu, zda je deska plná
def is_full(board):
    return " " not in board

# Hlavní funkce pro hru
def play_game():
    board = [" "] * 9
    current_player = "O"  # Začíná hráč O

    print("Welcome to Tic Tac Toe")
    print("="*40)
    print("GAME RULES:")
    print("Each player can place one mark (or stone) per turn on the 3x3 grid.")
    print("The WINNER is who succeeds in placing three of their marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("="*40)
    print("Let's start the game")
    print("-" * 40)

    while True:
        print_board(board)
        print(f"Player {current_player} | Please enter your move number (1-9):")

        move = int(input()) - 1  # Uživatel zadá číslo 1-9, které se přepočítá na index

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations, Player {current_player} WON!")
            break

        if is_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Střídání hráčů
        current_player = "X" if current_player == "O" else "O"

# Spuštění hry
if __name__ == "__main__":
    play_game()