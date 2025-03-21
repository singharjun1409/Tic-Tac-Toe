import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [[None for i in range(3)] for j in range(3)]
        self.buttons = [[None for i in range(3)] for j in range(3)]
        self.create_board()
    
    def create_board(self):
        # Creating the button grid
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="_", font=("Arial", 24), height=5, width=10,
                                                command= lambda row = i, col = j: self.make_move(row, col)) 
                self.buttons[i][j].grid(row=i, column=j)
    
    def make_move(self, row, col):
        # Ensuring valid move
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return
            self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self, player):
        # Checking for player win
        for i in range(3):
            # Row Win
            if all(self.board[i][j] == player for j in range(3)):  
                return True
            # Column Win
            if all(self.board[j][i] == player for j in range(3)):  
                return True
        # Diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
    
    def is_draw(self):
        # Checking if the game is a draw (board is full)
        return all(self.board[i][j] is not None for i in range(3) for j in range(3))
    
    def reset_board(self):
        # Board Reset 
        for i in range(3):
            for j in range(3):
                self.board[i][j] = None
                self.buttons[i][j].config(text="_", state=tk.NORMAL)
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
