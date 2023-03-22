const startButton = document.getElementById('start-button');
const gameBoard = document.querySelector('.game-board');

startButton.addEventListener('click', () => {
    startButton.style.display = 'none';
    gameBoard.style.display = 'block';
});

const clues = document.querySelectorAll('.clue');

clues.forEach((clue, index) => {
    clue.addEventListener('click', () => {
        if (index < clues.length - 1) {
            clue.style.display = 'none';
            clues[index + 1].style.display = 'block';
        } else {
            alert('Congratulations! You found the treasure!');
        }
    });
});