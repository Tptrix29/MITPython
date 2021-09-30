# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    for char in secret_word:
        if char not in letters_guessed:
            flag = False
    return flag


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    show_word = '_' * len(secret_word)
    show_word = list(show_word)
    for char in letters_guessed:
        ind = []
        st = 0
        while st <= len(secret_word):
            if secret_word[st:].find(char) == -1:
                break
            st += secret_word[st:].find(char) + 1
            ind.append(int(st) - 1)

        for i in ind:
            show_word[i] = char
    guessed_word = ''.join(show_word)
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_available = [chr(i) for i in range(97, 123)]
    for char in letters_guessed:
        if char in letter_available:
            letter_available.remove(char)
    return letter_available
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("The letter number of secret word is %d." % len(secret_word))
    letters = [chr(i) for i in range(97, 123)]

    # Start
    guessed_letters = []
    first_input = input("You should input 6 guesses at first: ")
    guessed_letters.extend(list(first_input))
    # input test
    while True:
        flag = False
        for i in guessed_letters:
            if str(i) not in letters:
                flag = True
        if flag:
            guessed_letters = []
            first_input = input("\nInput NOT letters!\nYou should input 6 guesses letters at first: ")
            guessed_letters.extend(list(first_input))
            continue
        else:
            break
    guessed_word = get_guessed_word(secret_word, guessed_letters)


    # Loop
    loop_count = 0
    while not is_word_guessed(secret_word, guessed_letters):
        print("\nThe word you have guessed: %s" % guessed_word)
        avai = get_available_letters(guessed_letters)
        print("Available letters:", avai)
        letter = input("\nPlease input a letter you want to guess: ")
        # input test
        while True:
            flag = False
            if letter not in avai:
                flag = True
            if flag:
                letter = input("\nInput ERROR!\nPlease input an available letter: ")
            else:
                guessed_letters.extend(letter)
                break
        guessed_word = get_guessed_word(secret_word, guessed_letters)
        loop_count += 1

    print("\n--------------------------Game Result-----------------------------")
    print("Congratulations!\nYou have guessed out the word \"%s\"!" % secret_word)
    print("You totally used %d loops to finish this game." % loop_count)

    return None



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = True
    if len(my_word) == len(other_word):
        for i in range(len(other_word)):
            if my_word[i] == '_':
                continue
            else:
                if not(other_word[i] == my_word[i]):
                    flag = False
                    break
    else:
        flag = False
    return flag


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
        if match_with_gaps(my_word, word):
            letter_guessed = set(list(my_word))
            letter_guessed.remove('_')
            flag = True
            for i in range(len(word)):
                if my_word[i] == '_':
                    if word[i] in letter_guessed:
                        flag = False
            if flag:
                print(word, end=' ')
    return None


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("The letter number of secret word is %d." % len(secret_word))
    letters = [chr(i) for i in range(97, 123)]

    # Start
    guessed_letters = []
    first_input = input("You should input 6 guesses at first: ")
    guessed_letters.extend(list(first_input))
    # input test
    while True:
        flag = False
        for i in guessed_letters:
            if str(i) not in letters:
                flag = True
        if flag:
            guessed_letters = []
            first_input = input("\nInput NOT letters!\nYou should input 6 guesses letters at first: ")
            guessed_letters.extend(list(first_input))
            continue
        else:
            break
    guessed_word = get_guessed_word(secret_word, guessed_letters)

    # Loop
    loop_count = 0
    while not is_word_guessed(secret_word, guessed_letters):
        print("\nThe word you have guessed: %s" % guessed_word)
        avai = get_available_letters(guessed_letters)
        print("Available letters:", avai)
        letter = input("\nPlease input a letter you want to guess (\"*\" for hint words): ")
        # input test
        while True:
            if letter == '*':
                print("-" * 150)
                print("Hint Words: ")
                show_possible_matches(guessed_word)
                print("\n" + "-" * 150)
                break
            else:
                flag = False
                if letter not in avai:
                    flag = True
                if flag:
                    letter = input("\nInput ERROR!\nPlease input an available letter (\"*\" for hint words): ")
                else:
                    guessed_letters.extend(letter)
                    if letter in secret_word:
                        print("This letter exists in secret word!")
                    else:
                        print("This letter does NOT exist in secret word!")
                    break

        guessed_word = get_guessed_word(secret_word, guessed_letters)
        loop_count += 1

    return None



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
