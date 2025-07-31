# Tic Tac Toe vs Computer (Medium Difficulty)
import random

# Defining variables
board = ["-","-","-","-","-","-","-","-","-"]
p1 = ""
p2 = ""
gameon = True
current_player = "X"

# Set player symbols, player vs computer by default
def players():
    global p1, p2
    p1 = input("Choose X or O: ").upper()
    while p1 not in ["X", "O"]:
        print("Invalid input. Type X or O.")
        p1 = input("Choose X or O: ").upper()
    p2 = "O" if p1 == "X" else "X"
    print("You are " + p1 + ". Computer is " + p2)

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2]+"    1|2|3")
    print(board[3]+"|"+board[4]+"|"+board[5]+"    4|5|6")
    print(board[6]+"|"+board[7]+"|"+board[8]+"    7|8|9")

def check_winner(symbol):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    for i, j, k in win_combos:
        if board[i] == board[j] == board[k] == symbol:
            return True
    return False

def computer_move():
    # 1. Try to win
    for i in range(9):
        if board[i] == "-":
            board[i] = p2
            if check_winner(p2):
                display_board()
                return
            board[i] = "-"

    # 2. Try to block
    for i in range(9):
        if board[i] == "-":
            board[i] = p1
            if check_winner(p1):
                board[i] = p2
                display_board()
                return
            board[i] = "-"

    # 3. Random move
    empty = [i for i, val in enumerate(board) if val == "-"]
    move = random.choice(empty)
    board[move] = p2
    display_board()

def player_pos():
    global current_player
    print("Current Player: " + current_player)

    if current_player == p2:
        print("Computer is thinking...")
        computer_move()
        return

    valid = False
    position = input("Choose from 1 - 9: ")

    while not valid:
        while position not in [str(n) for n in range(1, 10)]:
            position = input("Choose from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already occupied, choose different!")

    board[position] = current_player
    display_board()

def again():
    global gameon, board
    want = input("Wanna play again! y or n: ")
    if want == "y":
        print("Restart!")
        gameon = True
        board = ["-","-","-","-","-","-","-","-","-"]
        compgame()
    else:
        print("Ok, Bye!")

def compgame():
    players()
    display_board()

    global current_player, gameon

    while gameon:
        player_pos()

        def check_win():
            global gameon
            win_combos = [(0,1,2),(3,4,5),(6,7,8),
                          (0,3,6),(1,4,7),(2,5,8),
                          (0,4,8),(2,4,6)]
            for i, j, k in win_combos:
                if board[i] == board[j] == board[k] != "-":
                    print(board[i] + " WINS!")
                    gameon = False
                    again()
                    return
            if "-" not in board:
                print("It's a TIE!")
                gameon = False
                again()

        def flip():
            global current_player
            current_player = p2 if current_player == p1 else p1

        check_win()
        if gameon:
            flip()

