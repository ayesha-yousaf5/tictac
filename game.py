<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic-Tac-Toe</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        #gameBoard {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 5px;
        }
        .cell {
            width: 100px;
            height: 100px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 2rem;
            background-color: #fff;
            border: 2px solid #000;
            cursor: pointer;
        }
        #message {
            margin-top: 20px;
            font-size: 1.5rem;
        }
    </style>
</head>
<body>

    <div id="gameBoard">
        <div class="cell" data-index="0"></div>
        <div class="cell" data-index="1"></div>
        <div class="cell" data-index="2"></div>
        <div class="cell" data-index="3"></div>
        <div class="cell" data-index="4"></div>
        <div class="cell" data-index="5"></div>
        <div class="cell" data-index="6"></div>
        <div class="cell" data-index="7"></div>
        <div class="cell" data-index="8"></div>
    </div>
    <div id="message"></div>

    <script>
        const gameBoard = document.getElementById('gameBoard');
        const message = document.getElementById('message');
        const cells = document.querySelectorAll('.cell');
        let currentPlayer = 'X';
        let boardState = ['', '', '', '', '', '', '', '', ''];
        let gameActive = true;

        // Winning combinations
        const winningConditions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ];

        function handleCellClick(event) {
            const clickedCell = event.target;
            const clickedIndex = parseInt(clickedCell.getAttribute('data-index'));

            // If the cell is already filled or the game is inactive, return
            if (boardState[clickedIndex] !== '' || !gameActive) {
                return;
            }

            // Update the game state and UI
            boardState[clickedIndex] = currentPlayer;
            clickedCell.textContent = currentPlayer;

            checkWinner();
            togglePlayer();
        }

        function checkWinner() {
            let roundWon = false;

            for (let i = 0; i < winningConditions.length; i++) {
                const [a, b, c] = winningConditions[i];
                if (boardState[a] === '' || boardState[b] === '' || boardState[c] === '') {
                    continue;
                }
                if (boardState[a] === boardState[b] && boardState[b] === boardState[c]) {
                    roundWon = true;
                    break;
                }
            }

            if (roundWon) {
                message.textContent = `Player ${currentPlayer} wins!`;
                gameActive = false;
                return;
            }

            // Check for tie
            if (!boardState.includes('')) {
                message.textContent = "It's a tie!";
                gameActive = false;
                return;
            }
        }

        function togglePlayer() {
            currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
        }

        // Reset game
        function resetGame() {
            boardState = ['', '', '', '', '', '', '', '', ''];
            cells.forEach(cell => cell.textContent = '');
            currentPlayer = 'X';
            gameActive = true;
            message.textContent = '';
        }

        // Add click event listeners to each cell
        cells.forEach(cell => cell.addEventListener('click', handleCellClick));

        // Optionally, add a reset button
        const resetButton = document.createElement('button');
        resetButton.textContent = 'Reset Game';
        resetButton.onclick = resetGame;
        document.body.appendChild(resetButton);

    </script>

</body>
</html>
