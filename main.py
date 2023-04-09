from tkinter import *
from tkinter import ttk

def firstPlayerMove():
    while True:
        try:
            pile = int(input("Player 1, from what pile you want to take stones from?\n"))-1
            if pile < 0 or pile > len(piles) or piles[pile]<=0:
                print("Such pile does not exists or is empty")
            else:
                break
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            stonesTaken = int(input("Player 1, how many stones do you take?\n"))
            if stonesTaken > piles[pile] or stonesTaken < 1:
                print("Incorrect amount, try again")
            else:
                piles[pile]=piles[pile]-stonesTaken
                if sum(piles) <= 0:
                    print("PLAYER 1 WINS!")
                    return
                render()
                break
        except ValueError:
            print("Please enter a number.")
    
def secondPlayerMove():
    while True:
        try:
            pile = int(input("Player 2, from what pile you want to take stones from?\n"))-1
            if pile < 0 or pile > len(piles) or piles[pile]<=0:
                print("Such pile does not exists")
            else:
                break
        except ValueError:
            print("Please enter a number.")
    while True:
        try:
            stonesTaken = int(input("Player 2, how many stones do you take?\n"))
            if stonesTaken > piles[pile] or stonesTaken < 1:
                print("Incorrect amount, try again")
            else:
                piles[pile]=piles[pile]-stonesTaken
                if sum(piles) <= 0:
                    print("PLAYER 2 WINS!")
                    return
                render()
                break
        except ValueError:
            print("Please enter a number.")
    
def render():
    i=1
    for pile in piles:
        print(str(i)+") ",end="")
        for _ in range(pile):
            print("🗿",end="")
        print("\n")
        i=i+1

print("Greetings in the game of Nim!")
print("The rules are simple:")
print('There are N amount stones in each of 3 piles.')
print("Players take turns removing any number of stones.")
print("The player who removes the last stone wins.")
global piles, first_pile, second_pile, third_pile
piles = [first_pile, second_pile, third_pile] = [0,0,0]
for idx in range(3):
    while True:
        try:
            pile = int(input(f"How many stones do you want to be in pile Nº{idx+1}?\n"))
            if pile < 1:
                print("You must play with at least 1 stone. Try again.")
            else:
                piles[idx]=pile
                break
        except ValueError:
            print("Please enter a number.")


render()

while True:
    firstPlayerMove()
    if sum(piles) <=0: break
    secondPlayerMove()
    if sum(piles) <=0: break