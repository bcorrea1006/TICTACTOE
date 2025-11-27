import numpy as np

board = np.full((3, 3), ' ')

def main():
  current_player = 'X'
  turn = 0
  while turn < 9:
    display_board()
    print(f"Turn {turn}")
    row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
    if (row not in range(3) or col not in range(3) or board[row][col] != ' '):
      print("invalid move, try again.")
      turn -= 1
      continue
    board[row][col] = current_player
    if (check_winner(current_player)):
      return True
    current_player = 'O' if (current_player == 'X') else 'X'
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
