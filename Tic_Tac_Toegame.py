# game board
board = ["--", "--", "--",
        "--", "--", "--"
        "--", "--", "--"]
current_player = "X"
winner = None
game_running = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#player input
def player_input(board):
    inp = int(input("Select a number 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = current_player
    else:
        print("player is already at that spot. Try again")


# switch player
def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        currentPlayer = "X"
#check for win