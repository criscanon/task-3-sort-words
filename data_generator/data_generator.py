import random
import string

def generate_word(length):
    """
    Generate a random word with the specified length.
    
    Parameters:
    length (int): The length of the word.
    
    Returns:
    str: The randomly generated word.
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_word_list(num_words, word_length, sort):
    """
    Generate a list of random words with the specified length.
    
    Parameters:
    num_words (int): The number of words to generate.
    word_length (int): The length of each word.
    
    Returns:
    list: A list of randomly generated words.
    """

    word_list = []

    if sort == "random":  
        for _ in range(num_words):
            word = generate_word(word_length)
            word_list.append(word)
    elif sort == "sort":
        for _ in range(num_words):
            word = generate_word(word_length)
            word_list.append(word)
        word_list.sort()
    elif sort == "reverse":
        for _ in range(num_words):
            word = generate_word(word_length)
            word_list.append(word)
        word_list.reverse()

    return word_list
