import math
import sys

# Display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("____________")
    print("\n")

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def left(board):
    for row in board:
        if " " in row:
            return True
    return False

def minimax(board, depth, maximize):
    win = winner(board)

    if win == "O":  
        return 1
    elif win == "X":  
        return -1
    elif not left(board):  
        return 0

    if maximize:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    total = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(total, best_score)
        return best_score

    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    total = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(total, best_score)
        return best_score

# Find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                total = minimax(board, 0, False)
                board[i][j] = " "
                if total > best_score:
                    best_score = total
                    move = (i, j)
    return move

# Main game loop
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O.")
    print_board(board)

    while True:
        # Human turn
        while True:
            try:
                row = int(input("Enter the row number(1-3): ")) - 1
                col = int(input("Enter the column number (1-3): ")) - 1
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Its already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid! Enter numbers between 1 and 3.")

        print_board(board)

        if winner(board) == "X":
            print(" You won the Game,Congrats!")
            print("Thank You for Participating.")
            break
        if not left(board):
            print("It's a Tie!")
            print("Thank You for Participating.")
            break

        # AI turn
        print("Its AI Turn Now ...")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        print_board(board)

        if winner(board) == "O":
            print(" AI won the game! Better luck next time.")
            print("Thank You for Participating.")
            break
        if not left(board):
            print(" It's a tie!")
            print("Thank You for Participating.")
            break


if __name__ == "__main__":
    play()
