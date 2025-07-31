from computer import compgame
from player import maingame

print("Welcome to Tic-Tac-Toe")
print("Modes:\n1. Play with Computer\n2. Play with Friend\n3. About\n4. Exit")

def Modes():
    mode = int(input(">Select Mode: "))

    if mode == 1:
        compgame()
    elif mode == 2:
        maingame()
    elif mode == 3:
        print("Created by - One Sided\nRepo Link - https://github.com/TheOnesided/CLI-TicTacToe.git\nAbout Project - A simple yet polished CLI Tic Tac Toe game with a computer opponent. Built entirely on Android using Termux and GNOME. My first Python project.")
    elif mode == 4:
        print("Ok, Bye!")
    else:
        print("Invalid Input!")
        Modes()

Modes()