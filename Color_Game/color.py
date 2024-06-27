import tkinter as tk
import random

class ColorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Game")
        self.colors = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "Purple", "Brown", "Gray"]
        self.score = 0
        self.timeleft = 30

        self.instructions = tk.Label(master, text="Type in the color of the words, not the word text!", font=('Helvetica', 12))
        self.instructions.pack()

        self.score_label = tk.Label(master, text="Press Enter to start", font=('Helvetica', 12))
        self.score_label.pack()

        self.time_label = tk.Label(master, text="Time left: " + str(self.timeleft), font=('Helvetica', 12))
        self.time_label.pack()

        self.displayed_word = tk.Label(master, font=('Helvetica', 60))
        self.displayed_word.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind('<Return>', self.start_game)
        self.entry.focus_set()

    def start_game(self, event):
        if self.timeleft == 30:
            self.countdown()
        self.next_color()

    def next_color(self):
        if self.timeleft > 0:
            self.entry.focus_set()
            if self.entry.get().lower() == self.colors[1].lower():
                self.score += 1

            self.entry.delete(0, tk.END)
            random.shuffle(self.colors)
            self.displayed_word.config(fg=str(self.colors[1]), text=str(self.colors[0]))
            self.score_label.config(text="Score: " + str(self.score))


    def countdown(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.time_label.config(text="Time left: " + str(self.timeleft))
            self.master.after(1000, self.countdown)
        else:
            self.displayed_word.config(text="Game Over!", fg="black")
            self.score_label.config(text="Final Score: " + str(self.score))


# Create the main window
root = tk.Tk()
game = ColorGame(root)
root.mainloop()