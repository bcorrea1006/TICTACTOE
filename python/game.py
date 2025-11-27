import numpy as np

board = np.full((3, 3), ' ')

def main():
  current_player = 'X'
  for turn in range(9):
    # Print the turn number and board
    print(f"Turn {turn + 1}")
    display_board()
    # Get the user's input
    row, col = get_user_input(current_player)
    # Place the player's move
    board[row][col] = current_player
    if check_winner(current_player):
      return True
    # Toggle the current player
    current_player = 'O' if current_player == 'X' else 'X'
  # End the game in a tie if we've used all 9 turns
  display_board()
  print("Tie!")

def display_board():
  print()
  print('\n-----\n'.join('|'.join(row) for row in board))
  print()

def get_user_input(current_player):
  while True:
    try:
      row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
      row -= 1 # Convert to 0-based index
      col -= 1
    except ValueError:
      print("Please enter two numbers, separated by a space.")
      continue
    if row in range(3) and col in range(3) and board[row][col] == ' ':
      return row, col # return immediately when valid
    else:
      print("Invalid move. Row and column must be within range 1 - 3.")

def check_winner(player):
  # Check the rows and columns first
  for line in board, board.T:
    if any(all(cell == player for cell in row) for row in line):
      display_board()
      print(f"Player {player} wins!!")
      return True
  # Check the diagonals
  if all(board[i, i] == player for i in range(3)) or all(board[i, 2-i] == player for i in range(3)):
    display_board()
    print(f"Player {player} wins!!")
    return True

if __name__ == "__main__":
  main()
