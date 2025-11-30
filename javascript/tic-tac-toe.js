const readline = require('readline');

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
    // TODO: Get user input (row, col)
    let [row, col] = getUserInput();
    // TODO: Check the winner
    // TODO: Update board and toggle player
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

// TODO: handle invalid input, get the input etc.
function getUserInput() {
  // Create an interface for input and output
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  rl.question('What is your name? ', (answer) => {
    console.log(`Hello, ${answer}!`);
    rl.close(); // Close the readline interface after getting the answer
  });
}

// Call main to start the program
main();