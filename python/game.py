import numpy as np

board = np.full((3, 3), ' ')

def main():
  current_player = 'X'
  turn = 0
  while turn < 9:
    # Display the board and print the turn number
    print(f"Turn {turn + 1}")
    display_board()

    # Input loop for a valid move
    isValid = False
    while not isValid:
      try:
        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
      except ValueError:
        print("Please enter two numbers, separated by a space.")
        continue

      if row in range(3) and col in range(3) and board[row][col] == ' ':
        isValid = True
      else:
        print("Invalid move, try again.")

    # Place the player's move
    board[row][col] = current_player
    if (check_winner(current_player)):
      return True
    # Toggle the current player and update the turn counter
    current_player = 'O' if (current_player == 'X') else 'X'
    turn += 1
  # End the game in a tie if we've used all 9 turns
  display_board()
  print("Tie!")

def display_board():
  print()
  print('\n-----\n'.join(['|'.join(row) for row in board]))
  print()

def check_winner(player):
  for i in range(3):
    if all(board[i, j] == player for j in range(3)) or all(board[j, i] == player for j in range(3)):
      display_board()
      print(f"Player {player} wins!")
      return True
  if all(board[i, i] == player for i in range(3)) or all(board[i, 2 - i] == player for i in range(3)):
    display_board()
    print(f"Player {player} wins!")
    return True
  return False

if __name__ == "__main__":
  main()
