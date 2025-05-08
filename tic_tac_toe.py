import tkinter as tk
from tkinter import messagebox
import math

HUMAN = "O"
AI = "X"
EMPTY = " "

board = [EMPTY for _ in range(9)]

def check_winner(brd, player):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_combos)

def is_draw(brd):
    return EMPTY not in brd and not check_winner(brd, HUMAN) and not check_winner(brd, AI)

def minimax_alpha_beta(brd, depth, alpha, beta, is_maximizing):
    if check_winner(brd, AI):
        return 10 - depth
    elif check_winner(brd, HUMAN):
        return depth - 10
    elif is_draw(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == EMPTY:
                brd[i] = AI
                score = minimax_alpha_beta(brd, depth + 1, alpha, beta, False)
                brd[i] = EMPTY
                max_eval = max(max_eval, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == EMPTY:
                brd[i] = HUMAN
                score = minimax_alpha_beta(brd, depth + 1, alpha, beta, True)
                brd[i] = EMPTY
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return min_eval

def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax_alpha_beta(board, 0, -math.inf, math.inf, False)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                move = i
    return move

# ---------------- GUI Part -------------------
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

buttons = []

def on_click(index):
    if board[index] != EMPTY:
        return

    board[index] = HUMAN
    buttons[index].config(text=HUMAN, state="disabled")

    if check_winner(board, HUMAN):
        messagebox.showinfo("Game Over", "🎉 You win!")
        root.quit()
    elif is_draw(board):
        messagebox.showinfo("Game Over", "🤝 It's a draw!")
        root.quit()
    else:
        ai_index = best_move()
        board[ai_index] = AI
        buttons[ai_index].config(text=AI, state="disabled")

        if check_winner(board, AI):
            messagebox.showinfo("Game Over", "😈 AI wins!")
            root.quit()
        elif is_draw(board):
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            root.quit()

def restart_game():
    global board, buttons
    board = [EMPTY for _ in range(9)]
    for i in range(9):
        buttons[i].config(text="", state="normal")

# Draw board
for i in range(9):
    btn = tk.Button(root, text="", width=8, height=4, font=("Arial", 20), command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Restart Button
restart = tk.Button(root, text="Restart", command=restart_game, font=("Arial", 12))
restart.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
