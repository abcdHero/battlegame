# Number Punch 數字拳

This is a simple game similar to Rock-Paper-Scissors but with more elements. Each player can show either 1, 2, 3, 4 or 5. The larger is a winner except 1 wins over 5.

## Requirements
1. The game is built in Python 3.
2. The game is built with [pygame](https://www.pygame.org/).
```shell
pip3 install pygame
```
3. You'd better run in a virtual environment for a separate codebase. Ref: [venv](https://docs.python.org/3/tutorial/venv.html)

## How to run
```shell
python3 number_punch.py
```

## How to play
1. Enter the main menu
2. Player 1 presses W to increase his value; S to decrease his value
3. Player 2 presses UP key to increase his value; DOWN to decrease his value
4. Both values are from 1 to 5, recycled.
5. If both players are ready, press ENTER to confirm
6. Wait for the result
7. Then play again or close the window to quit the game