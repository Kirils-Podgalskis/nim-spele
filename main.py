from node import *
from functions import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys
import os

window = Tk()
window.title("Nim Game")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width*0.75
window_height = screen_height*0.75
window.resizable(width=False, height=False)
window.configure(bg="#0C2D48")

# function that is called if user decides to restart the game
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

title_label= tk.Label(master=window, text="Nim Game", font=("Arial", 30),bg="#6699CC", fg="#CDDEEE")
title_label.grid(row=0, column=0, columnspan=3,sticky='ew')

rules_label = tk.Label(master=window, text="Rules: \n1. There are 3 piles of stones. \n2. You can take any amount of stones from any, but only one pile. \n3. The player who takes the last stone wins.", font=("Arial", 15), bg="#4482C1", fg="#CDDEEE")
rules_label.grid(row=1, column=0, rowspan=2,sticky='ew')

question_label = tk.Label(master=window, text="Who goes first?", font=("Arial", 15), bg="#366BA1", fg="#CDDEEE")
question_label.grid(row=1,column=1,rowspan=2,sticky='ewns')

# radio buttons for choosing who goes first
first_move = StringVar()
Radiobutton(window, text="Human", variable=first_move,bg="#ABC7E3",fg="#2A547E", value="human").grid(row=1, column=2,sticky='ew')
Radiobutton(window, text="Computer", variable=first_move,bg="#ABC7E3",fg="#2A547E", value="computer").grid(row=2, column=2,sticky='ew')

for i in range(3):
        question=f"How many stones in pile No.{i+1}?"
        tk.Label(master=window, text=question,font=("Arial", 15),bg="#145DA0",fg="#CDDEEE").grid(row=3, column=i)

# pile definition input boxes
first_input= Entry(window)
first_input.grid(row=4, column=0,sticky='ew')

second_input= Entry(window)
second_input.grid(row=4, column=1,sticky='ew')

third_input= Entry(window)
third_input.grid(row=4, column=2,sticky='ew')

# function that starts the game and clear Menu screen
def submit():
    # error handling
    try:
        first_pile = int(first_input.get())
        second_pile = int(second_input.get())
        third_pile = int(third_input.get())
        if first_pile < 1 or second_pile < 1 or third_pile < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid number of stones\nPlease enter a positive integer")
        return

    piles = [first_pile,second_pile,third_pile]
    player = first_move.get()

    for widget in window.winfo_children():
        widget.destroy()

    play_game(piles, player)

start_game_btn = tk.Button(master=window,height=3, text="Start Game", bg="#AE87BA",fg="#CDDEEE", command=submit)
start_game_btn.grid(row=5, column=1,sticky='ewns', rowspan=3)

# function that checks if the game is over
def check_win(piles, player):
    if all(p == 0 for p in piles):
        for widget in window.winfo_children():
            widget.destroy()
        if player == "human":
            you_won_label = tk.Label(master=window, text="You Won!", font=("Arial", 30),bg="#333652",fg="#FAD02C")
            you_won_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            you_lost_label = tk.Label(master=window, text="You Lost!", font=("Arial", 30),bg="#333652",fg="#FAD02C")
            you_lost_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        restart_btn = tk.Button(master=window, text="Restart", command=restart_program)
        restart_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
        return True
    return False

# core function of the game, it is called recursively and executes the game and the minimax algorithm if the player is the computer
def play_game(piles,player):
    render(piles)
    if player == "human":
        #function that clears the input boxes when clicked
        def pile_temp(e):
            pile_input.delete(0,"end")
        def stones_temp(e):
            stones_input.delete(0,"end")

        #input boxes
        pile_input= Entry(window)
        pile_input.insert(0, "Enter pile's number")
        pile_input.bind("<FocusIn>", pile_temp)
        pile_input.grid(row=2, column=1, columnspan=2,sticky='ew')

        stones_input= Entry(window)
        stones_input.insert(0, "Enter number of stones")
        stones_input.bind("<FocusIn>", stones_temp)
        stones_input.grid(row=3, column=1, columnspan=2,sticky='ew')

        #function that allows the user to take stones
        def take():
            pile_idx = int(pile_input.get())-1
            amount = int(stones_input.get())
            #error handling
            if pile_idx < 0 or pile_idx > 2:
                messagebox.showerror("Error", "Invalid pile number")
                return
            if amount < 1 or amount > piles[pile_idx]:
                messagebox.showerror("Error", f"Invalid number of stones\nYou can only take between 1 and {piles[pile_idx]} stones")
                return

            piles[pile_idx] -= amount

            if check_win(piles, player): return  

            new_player = "computer"
            play_game(piles, new_player)

        take_btn = tk.Button(master=window, text="Take", bg="green", command=take)
        take_btn.grid(row=4, column=0,columnspan=3,sticky='ew')
    else:
        root_node = Node(piles, "Max")
        generate_children(root_node, depth=2)
        minimax(root_node, depth=2, is_max=True)
        previous_state = piles
        piles = root_node.move
        for i in range(3):
            if piles[i] != previous_state[i]:
                messagebox.showinfo("Computer's move", f"Computer took {previous_state[i] - piles[i]} stones from pile No.{i+1}")
                break
        if check_win(piles, player): return

        new_player = "human"
        play_game(piles, new_player)

# function to render current state of the game
def render(piles):
    title_label= tk.Label(master=window, text="Nim Game", font=("Arial", 30),bg="#6699CC", fg="#CDDEEE")
    title_label.grid(row=0, column=0, columnspan=3, sticky='ew')

    pick_label = tk.Label(master=window,width=17, text="Pick a pile:", font=("Arial", 15), bg="#2E8BC0")
    pick_label.grid(row=2, column=0, sticky='ew')

    stones_label = tk.Label(master=window,width=17, text="Pick a number of stones:", font=("Arial", 15), bg="#2E8BC0")
    stones_label.grid(row=3, column=0, sticky='ew')

    for i in range(3):
        tk.Label(master=window, text=str(piles[i])+f"\nPile No.{i+1}", width=17,height=3, relief=RAISED, font=("Helvetica",20,"bold") ,bg="#0C2D48", fg="#B1D4E0").grid(row=1, column=i,sticky='ew')
    window.update()

window.mainloop()