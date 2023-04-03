from tkinter import *
from tkinter import ttk

stones = 10
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
print(f'There are {stones} stones in the pile.')
print("Players take turns removing 1, 2, or 3 stones.")
print("The player who removes the last stone wins.")
render()

while True:
    firstPlayerMove()
    if stones <=0: break
    secondPlayerMove()
    if stones <=0: break