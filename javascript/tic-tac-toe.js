let board = [
  [' ', ' ', ' '],
  [' ', ' ', ' '],
  [' ', ' ', ' ']
]

function main() {
  current_player = 'X'
  for (let turn = 0; turn < 9; turn++) {
    console.log("Turn " + (turn + 1))
    displayBoard();
    // Get user input (row, col)
    let [row, col] = getUserInput();
    // Check the winner
    // Update board and toggle player
    board[row][col] = current_player;
    current_player = current_player == 'X' ? 'O' : 'X';
  }
  displayBoard();
  console.log("Tie!")
}

function displayBoard() {
  let rows = board.map(row => {
    return row.join("|");
  })
  console.log();
  console.log(rows.join("\n-----\n"));
  console.log();
}

function getUserInput() {
  return [2, 1];
}

// Call main to start the program
main();