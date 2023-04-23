from tkinter import *
from tkinter import ttk, messagebox
import random

root = Tk()
root.title("Minenräumer")

# Creating the style and setting the theme
style = ttk.Style()
style.theme_use('classic')

#A list of buttons and a boolean list to track which buttons have mines .
buttons = [Button(root, text='') for i in range(16)]
has_mine = [False for i in range(16)]

# Placing the buttons in a grid
for i in range(4):
    for j in range(4):
        button_index = i * 4 + j
        button = buttons[button_index]
        button.grid(row=i, column=j, sticky='snew', ipadx=40, ipady=40)
        button.config(command=lambda index=button_index: button_click(index))

# Randomly selecting a button that has a mine
mine_index = random.randint(0, 15)
has_mine[mine_index] = True

# Variables for tracking the game state.
click_count = 0
game_over = False


def button_click(index):
    global click_count, game_over

    if game_over:
        return

    button = buttons[index]

    if has_mine[index]:
        # Spiel verloren
        button.config(bg="red", state=DISABLED)
        show_message("Du hast verloren!")
        game_over = True
    else:
        # Incrementing the click counter and checking if the player has won.
        click_count += 1
        button.config(state=DISABLED)
        if click_count == 5:
            show_message("Du hast gewonnen!")
            game_over = True


def show_message(message):
    # Displaying the message in a pop-up dialog box.
    messagebox.showinfo("Spiel beendet", message)


root.mainloop()
