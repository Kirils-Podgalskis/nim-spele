from node import *
from functions import *
import tkinter as tk
from tkinter import *
import sys
import os

window = Tk()
window.title("Nim Game")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = screen_width*0.75
window_height = screen_height*0.75
window.resizable(width=False, height=False)
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

title_label= tk.Label(master=window, text="Nim Game", font=("Arial", 30),background="blue")
title_label.grid(row=0, column=0, columnspan=3,sticky='ew')

rules_label = tk.Label(master=window, text="Rules: \n1. There are 3 piles of stones. \n2. You can take any amount of stones from any, but only one pile. \n3. The player who takes the last stone wins.", font=("Arial", 15), background="red")
rules_label.grid(row=1, column=0, rowspan=2,sticky='ew')

question_label = tk.Label(master=window, text="Who goes first?", font=("Arial", 15), background="green")
question_label.grid(row=1,column=1,rowspan=2,sticky='ew')

first_move = StringVar()
Radiobutton(window, text="Human", variable=first_move, value="human").grid(row=1, column=2,sticky='ew')
Radiobutton(window, text="Computer", variable=first_move, value="computer").grid(row=2, column=2,sticky='ew')

for i in range(3):
        question=f"How many stones in pile No.{i+1}?"
        tk.Label(master=window, text=question).grid(row=3, column=i)

first_input= Entry(window)
first_input.grid(row=4, column=0,sticky='ew')

second_input= Entry(window)
second_input.grid(row=4, column=1,sticky='ew')

third_input= Entry(window)
third_input.grid(row=4, column=2,sticky='ew')

def submit():
    first_pile = int(first_input.get())
    second_pile = int(second_input.get())
    third_pile = int(third_input.get())

    piles = [first_pile,second_pile,third_pile]
    player = first_move.get()

    for widget in window.winfo_children():
        widget.destroy()

    play_game(piles, player)

start_game_btn = tk.Button(master=window, text="Start Game", background="green", command=submit)
start_game_btn.grid(row=5, column=1,sticky='ew', rowspan=3)

def check_win(piles, player):
    if all(p == 0 for p in piles):
        for widget in window.winfo_children():
            widget.destroy()
        if player == "human":
            you_won_label = tk.Label(master=window, text="You Won!", font=("Arial", 30),background="blue")
            you_won_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        else:
            you_lost_label = tk.Label(master=window, text="You Lost!", font=("Arial", 30),background="blue")
            you_lost_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        restart_btn = tk.Button(master=window, text="Restart", background="green", command=restart_program)
        restart_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
        return True
    return False

def play_game(piles,player):  # Starting piles and who goes first
    render(piles)
    if player == "human":
        pile_input= Entry(window)
        pile_input.grid(row=2, column=1, columnspan=2,sticky='ew')

        stones_input= Entry(window)
        stones_input.grid(row=3, column=1, columnspan=2,sticky='ew')

        def take():
            pile_idx = int(pile_input.get())-1
            amount = int(stones_input.get())
            if pile_idx < 0 or pile_idx > 2:
                return
            if amount < 1 or amount > piles[pile_idx]:
                return
            piles[pile_idx] -= amount
            
            if check_win(piles, player): return  

            new_player = "computer"
            play_game(piles, new_player)

        take_btn = tk.Button(master=window, text="Take", background="green", command=take)
        take_btn.grid(row=4, column=0,columnspan=3,sticky='ew')
    else:
        root_node = Node(piles, "Max")
        generate_children(root_node, depth=2)
        minimax(root_node, depth=2, is_max=True)
        print(root_node)
        piles = root_node.move

        if check_win(piles, player): return

        new_player = "human"
        play_game(piles, new_player)

def render(piles):
    title_label= tk.Label(master=window, text="Nim Game", font=("Arial", 30),background="blue")
    title_label.grid(row=0, column=0, columnspan=3, sticky='ew')

    pick_label = tk.Label(master=window,width=17, text="Pick a pile", font=("Arial", 15), background="gray")
    pick_label.grid(row=2, column=0, sticky='ew')

    stones_label = tk.Label(master=window,width=17, text="Pick a number of stones", font=("Arial", 15), background="gray")
    stones_label.grid(row=3, column=0, sticky='ew')

    for i in range(3):
        tk.Label(master=window, text=str(piles[i]), width=6,height=3, relief=RAISED, font=("Helvetica",36,"bold") ,background="black").grid(row=1, column=i,sticky='ew')
    window.update()

window.mainloop()