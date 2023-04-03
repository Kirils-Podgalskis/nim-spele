from tkinter import *
from tkinter import ttk

def firstPlayerMove():
    print("Player 1, how many stones do you take?")
    while True:
        try:
            stonesTaken = int(input())
            if stonesTaken > 3 or stonesTaken < 1:
                print("You can only take 1, 2, or 3 stones. Try again.")
            else:
                global stones
                stones = stones - stonesTaken
                if stones <= 0:
                    print("PLAYER 1 WINS!")
                    return
                render()
                break
        except ValueError:
            print("Please enter a number.")
    
def secondPlayerMove():
    print("Player 2, how many stones do you take?")
    while True:
        try:
            stonesTaken = int(input())
            if stonesTaken > 3 or stonesTaken < 1:
                print("You can only take 1, 2, or 3 stones. Try again.")
            else:
                global stones
                stones = stones - stonesTaken
                if stones <= 0:
                    print("PLAYER 2 WINS!")
                    return
                render()
                break
        except ValueError:
            print("Please enter a number.")
    
def render():
    for s in range(stones):
        print("🗿",end="")
    print("\n")

print("Greetings in the game of Nim!")
print("The rules are simple:")
print('There are N amount stones in the pile.')
print("Players take turns removing 1, 2, or 3 stones.")
print("The player who removes the last stone wins.")
print("How many stones do you want to play with?")
while True:
    try:
        global stones
        stones = int(input())
        if stones < 4:
            print("You must play with at least 4 stone. Try again.")
        else:
            break
    except ValueError:
        print("Please enter a number.")
render()

while True:
    firstPlayerMove()
    if stones <=0: break
    secondPlayerMove()
    if stones <=0: break