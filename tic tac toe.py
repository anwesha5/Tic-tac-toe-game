import tkinter as tk

# Create the game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Initialize variables
current_player = 'X'
winner = False
num_turns = 0

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Define the callback function for each button click
def button_click(row, col):
    global current_player, winner, num_turns
    if board[row][col] == ' ' and not winner:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        num_turns += 1
        if check_win(current_player):
            winner = True
            status_label.config(text=f"Player {current_player} wins!")
        elif num_turns == 9:
            status_label.config(text="It's a tie!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            status_label.config(text=f"Player {current_player}'s turn")

# Define the function to check for a win
def check_win(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or \
           board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Create the game board buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=' ', font=('Arial', 32), width=3, height=1, command=lambda row=i, col=j: button_click(row, col))
        button.grid(row=i, column=j, sticky='nsew')
        row.append(button)
    buttons.append(row)

# Create the status label
status_label = tk.Label(root, text=f"Player {current_player}'s turn", font=('Arial', 16), pady=10)
status_label.grid(row=3, column=0, columnspan=3)

# Configure the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

# Start the main event loop
root.mainloop()
