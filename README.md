# Hangman Game

This is a classic Hangman game implemented in Python as part of the CS50 Python course. The game randomly selects a word from a provided list and allows the player to guess letters until they either correctly guess the word or run out of attempts.

## How to Play

1. Run the `project.py` file.
2. The game will display a blank word represented by underscores (`_`).
3. Guess letters one at a time by typing them in when prompted.
4. If the guessed letter is in the word, it will be revealed in the correct position(s).
5. If the guessed letter is not in the word, a part of the hangman is drawn.
6. The game continues until you either guess the word correctly or the hangman is fully drawn.

## Word List

The game uses a custom word list located in `words.txt`. This word list was sourced from [Xethron's Hangman project on GitHub](https://github.com/Xethron/Hangman). The list contains a wide range of words that the game randomly selects from.

## Project Structure

- `project.py`: Main script to run the Hangman game.
- `words.txt`: Text file containing the list of words used in the game.
- `words.py`: Script managing the list of words that have been used in the game.
- `test_project.py`: Test script to validate the core functionality of the Hangman game.
- `requirements.txt`: File listing any pip-installable libraries required for the project.

## Installation

To run the game, simply clone this repository and run the `project.py` file using Python:

```bash
git clone https://github.com/DanaPacatang/hangman
cd hangman
python project.py
```

## Testing
The project includes a test suite in test_project.py that verifies the functionality of the game components. To run the tests, use:

```bash
pytest test_project.py
```

## Video Demo
A video demo of the project can be [viewed here](youtube.com).

## Credits
This project is a part of the [CS50 Python course](https://www.edx.org/learn/python/harvard-university-cs50-s-introduction-to-programming-with-python).

The word list used in this project was sourced from [Xethron's Hangman project on GitHub](https://github.com/Xethron/Hangman).
