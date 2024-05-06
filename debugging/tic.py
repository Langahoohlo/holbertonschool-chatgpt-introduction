#!/usr/bin/python3

def print_board(board):
    print("  0 | 1 | 2 ")
    print("–––|–––|–––")
    for i in range(3):
        print(f"{i} | {' | '.join(board[i])} |")
        print("–––|–––|–––")

def check_winner(board):
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True

    for col in range(len(board[0])):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    print_board(board)
    while not check_winner(board):
        row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input! Row and column values must be between 0 and 2.")

    print("Player " + player + " wins!")

tic_tac_toe()

