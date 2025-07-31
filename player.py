import random
# Defining variables
board = ["-","-","-","-","-","-","-","-","-"]
p1 = ""
p2 = ""
gameon = True
current_player = "X"

def players():
    #Choosing players
    global p1, p2
    p1 = input("Choose X or O: ").upper()
    p2 = ""

    if p1 == "X":
        p2 = "O"
        print("Player 2: " + p2)
        return p1, p2
    elif p1 == "O":
        p2 = "X"
        print("Player 2: " + p2)
        return p1, p2
    else:
        print("Sorry! invalid input. Type X or O.")
        players()

def display_board():
    #Drawing Board
    print(board[0]+"|"+board[1]+"|"+board[2]+"    "+"1|2|3\n"+board[3]+"|"+board[4]+"|"+board[5]+"    "+"4|5|6\n"+board[6]+"|"+board[7]+"|"+board[8]+"    "+"7|8|9")

def player_pos():
    global current_player
    valid = False
    print("Current Player: "+current_player)
    position = input("Choose from 1 - 9: ")
    
    #Loop through the game
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
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
        maingame()
    else:
        print("Ok, Bye!")

def maingame():
    players()
    display_board()

    while gameon:
        player_pos()

        #Check Winner
        def check_win():
            global gameon
            win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
            for i, j, k in win_combos:
                if board[i] == board[j] == board[k] != "-":
                    print(board[i] + " You WON!")
                    gameon = False
                    again()
                    return
            if "-" not in board:
                print("It's a TIE!")
                gameon = False
                again()

        def flip():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
                    
        check_win()
        flip()


