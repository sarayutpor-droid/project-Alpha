import tkinter as tk
from tkinter import messagebox

class OXGame:
    def __init__(self, root):
        self.root = root
        self.root.title("O X Game")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 32), width=4, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def on_click(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # cols
            [0,4,8], [2,4,6]           # diags
        ]
        for pattern in win_patterns:
            a, b, c = pattern
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = OXGame(root)
    root.mainloop()
