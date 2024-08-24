def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    for condition in win_conditions:
        if condition.count(player) == 3:
            return True
    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move // 3][move % 3] != " ":
                print("This spot is already taken. Please choose another spot.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    while True:
        # Initialize the board
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        # Main game loop
        while True:
            print_board(board)
            move = get_player_move(board, current_player)
            board[move // 3][move % 3] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
