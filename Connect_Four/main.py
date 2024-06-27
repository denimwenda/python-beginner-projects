import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1
        self.create_widgets()

    def create_widgets(self):
        self.buttons = []
        for col in range(7):
            button = tk.Button(self.master, text=f"Drop {col+1}", command=lambda col=col: self.drop_disc(col))
            button.grid(row=0, column=col)
            self.buttons.append(button)

        self.cells = []
        for row in range(1, 7):
            row_cells = []
            for col in range(7):
                cell = tk.Label(self.master, text="", width=4, height=2, borderwidth=2, relief="groove", bg="white")
                cell.grid(row=row, column=col)
                row_cells.append(cell)
            self.cells.append(row_cells)


    def drop_disc(self, col):
        for row in range(5, -1, -1):
            if self .board[row][col] == 0:
                self.board[row][col] = self.current_player
                self.cells[row][col].config(bg="red" if self.current_player == 1 else "yellow")
                if self.check_winner(row, col):
                    messagebox.showinfo("Connect Four", f"Player {self.current_player} wins!")
                    self.reset_board()
                else:
                    self.current_player = 3 - self.current_player
                return
            

    def check_winner(self, row,col):
        def count_discs(delta_row, delta_col):
            count = 0
            r, c = row, col
            while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.current_player:
                count += 1
                r += delta_row
                c += delta_col
            return count
        
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for dr, dc in directions:
            if count_discs(dr, dc) + count_discs(-dr, -dc) - 1 >= 4:
                return True
        return False
    
    def reset_board(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        for row in range(6):
            for col in range(7):
                self.cells[row][col].config(bg="white")
        self.current_player = 1


# Create the main window
root = tk.Tk()
game = ConnectFour(root)
root.mainloop()