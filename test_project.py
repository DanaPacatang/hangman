from project import hangman, get_word, display_word, guess


def test_get_word():
    # Test if it returns a lowercase word
    global words_list
    words_list = []
    
    selected_word = get_word()
    
    assert isinstance(selected_word, str), "Returned value is not a string"
    assert selected_word.islower(), "Returned value is not in lowercase"


def test_display_word():
    selected_word = "apple"
    
    # Test when no guesses have been made
    assert display_word(selected_word) == "_____"
    
    # Test with incorrect guesses
    assert display_word(selected_word, set(["x"])) == "_____"
    
    # Test with some correct guesses
    assert display_word(selected_word, set(["a"])) == "a____"
    assert display_word(selected_word, set(["a", "e"])) == "a___e"
    
    # Test with all letters guessed correctly
    assert display_word(selected_word, set(["a", "p", "l", "e"])) == "apple"


def test_guess():
    selected_word = "apple"
    
    # Test with correct guesses
    assert guess(selected_word, "a") == True
    assert guess(selected_word, "p") == True
    assert guess(selected_word, "l") == True
    assert guess(selected_word, "e") == True
    
    # Test with incorrect guesses
    assert guess(selected_word, "w") == False
    assert guess(selected_word, "x") == False
    assert guess(selected_word, "y") == False
    assert guess(selected_word, "z") == False