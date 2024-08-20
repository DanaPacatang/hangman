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

selected_word = ""
progress = ""
tries = 0


def hangman(i=0):
    return HANGMANPICS[i]


def get_word():
    global selected_word
    web2lowerset = get_english_words_set(['web2'], lower=True)
    word_list = list(web2lowerset)
    
    while True:
        selected_word = random.choice(word_list)
        
        if selected_word not in words_list:
            words_list.append(selected_word)
            return selected_word


def display_word(selected_word, guesses=None):
    global progress
    if guesses is None:
        guesses = ""
        
    if not guesses:
        progress = "_" * len(selected_word)
    else:
        progress = ''.join([letter if letter in guesses else '_' for letter in selected_word])
    
    return progress


def guess(selected_word, letter):
    return letter in selected_word


def main():
    global tries
    global progress
    
    get_word()
    
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
            print(hangman(tries) + "\n")
            print(display_word(selected_word, guessed_letters) + "\n")
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