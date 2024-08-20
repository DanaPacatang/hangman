from english_words import get_english_words_set
from words import words_list
import random


HANGMANPICS = [r'''
    +---+
    |   |
        |
        |
        |
        |
    =========''', r'''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', r'''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', r'''
    +---+
    |   |
    O   |
    /|  |
        |
        |
    =========''', r'''
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========''', r'''
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========''', r'''
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
    =========''']


def hangman(i=0):
    return HANGMANPICS[i]


def get_word():
    with open("words.txt", "r") as file:
        word_list = [line.strip() for line in file if line.strip()]
    
    while True:
        selected_word = random.choice(word_list)
        
        if selected_word not in words_list:
            words_list.append(selected_word)
            return selected_word


def display_word(selected_word, guesses=None):
    if guesses is None:
        guesses = set()
    
    return ''.join([letter if letter in guesses else '_' for letter in selected_word])


def guess(selected_word, letter):
    return letter in selected_word


def main():
    tries = 0
    selected_word = get_word()
    progress = "_" * len(selected_word)
    
    print(hangman() + "\n")
    print(display_word(selected_word) + "\n")
    
    guessed_letters = set()
    
    while tries < len(HANGMANPICS) - 1 and "_" in progress:
        guess_letter = input("Enter your guess: ").lower()
        
        if guess_letter in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess_letter)
        
        if guess(selected_word, guess_letter):
            progress = display_word(selected_word, guessed_letters)
            print(hangman(tries) + "\n")
            print(progress + "\n")
        else:
            tries += 1
            print(hangman(tries) + "\n")
            print(display_word(selected_word, guessed_letters) + "\n")
    
    if "_" not in progress:
        print("Congratulations, you won!")
    else:
        print(f"Game over! The word was {selected_word}.")


if __name__ == "__main__":
    main()
