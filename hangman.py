# # Problem Set 2, hangman.py
# # Name: Travis Cahill


# # Hangman Game
# # -----------------------------------
# # Helper code
# # You don't need to understand this helper code,
# # but you will have to know how to use the functions
# # (so be sure to read the docstrings!)
#
import random
import string
#
WORDLIST_FILENAME = "words.txt"
#
#
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
#
# # end of helper code
#
# # -----------------------------------
#
# # Load the list of words into the variable wordlist
# # so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # COME BACK TO THIS AND TRY TO WRITE THE LONGER VERSION OF THIS WHILE LOOP FOR PRACTICE

    #covnert the secret word to a list
    secret_word_list = list(secret_word)

    #compare the letterse guessed to the letters in your newly created secret word list,
    #this is the string converted to a list, if user guessed all of the letters in the secret word, print a boolean
    word_guessed_check = all(elem in letters_guessed for elem in secret_word_list)
    if word_guessed_check == True:
         return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    outputMessage = ""
    for letter in secret_word:
        if letter in letters_guessed:
            outputMessage += (letter + " ")
        else:
            outputMessage += ("_ ")

    return (outputMessage)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    rawAlphabet = "abcdefghijklmnopqrstuvwxyz"
    stringLettersGuessed = ''.join(letters_guessed)
    availableLetters = rawAlphabet
    for letters in stringLettersGuessed:
        availableLetters = availableLetters.replace(letters, "")
    return(availableLetters)


#keep track of erroneous keystrokes/characters and give warnings, there are 3 warnings,
#if out of warnings, user loses a guess


def guessesRemaining(letters_guessed,numGuesses,secret_word):
    '''letters guessed is a list of letters, used to count how many rounds you've guessed
    numGuesses is the max number of guesses
    if a letter guessed is in the secret word, it doesnt count toward your max number of guesses
    if a letter isn't in the secret word, it does count
    this function takes in the letters guessed checks if the letter is 'good' or 'bad' and compares it against numGuesses
    to see how many guesses you have remaining'''

    goodLetters = 0
    badLetters = 0

    for letter in letters_guessed:
        if letter in secret_word:
            goodLetters +=1
        else:
            badLetters += 1
    if badLetters == numGuesses:
        print(f"The word was {secret_word}. Unfortunately, you're out of guesses, off too the gallows with you.")
    else:
        print(f"You've not guessed the word yet. You have {(numGuesses - badLetters)} guesses remaining")

def guessesTrueFalse(letters_guessed,numGuesses,secret_word):
    '''letters guessed is a list of letters, used to count how many rounds you've guessed
    numGuesses is the max number of guesses
    if a letter guessed is in the secret word, it doesnt count toward your max number of guesses
    if a letter isn't in the secret word, it does count
    this function takes in the letters guessed checks if the letter is 'good' or 'bad' and compares it against numGuesses
    to see how many guesses you have remaining'''

    goodLetters = 0
    badLetters = 0

    for letter in letters_guessed:
        if letter in secret_word:
            goodLetters +=1
        else:
            badLetters += 1
    if badLetters == numGuesses:
        return True
    else:
        return False

def getLettersFromUser(letters_guessed,numGuesses):
    ''''''

    # user can ONLY input a letter they haven't already guessed
    # tell them they didnt guess a letter if they input a character or a number


    lettersGuessedInput = ""
    while (is_word_guessed(secret_word,letters_guessed) == False) and (guessesTrueFalse(letters_guessed,numGuesses,secret_word) == False):
        while (lettersGuessedInput.isalpha() == False) or (len(lettersGuessedInput) > 1):
            lettersGuessedInput = input("Please guess a letter ")
        lettersGuessedInputLowercase = lettersGuessedInput.lower()
        letters_guessed.append(lettersGuessedInputLowercase)
        break
    return letters_guessed


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

    numGuesses = 10
    letters_guessed = []
    print("Welcome to Hangman!")
    print(f"Your word has {len(secret_word)} characters, guess the letters correctly and you win.")
    print(f"You have {numGuesses} guesses, should you fail to guess the word, you'll hang!")
    get_guessed_word(secret_word, letters_guessed)

    while guessesTrueFalse(letters_guessed,numGuesses,secret_word) == False:
        if is_word_guessed(secret_word,letters_guessed) == False:
            getLettersFromUser(letters_guessed, numGuesses)
            print()
            print()
            guessesRemaining(letters_guessed, numGuesses, secret_word)
            print(f"Choose from these letters: {get_available_letters(letters_guessed)}")
            print()
            print(get_guessed_word(secret_word, letters_guessed))
            print()
            print("_____________________________________________________________")
            print()
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print()
            print()
            print()
            print("You've beat me!")
            print()
            print()
            print()
            break

# If the player runs out of guesses before completing the word, tell them they
# lost and reveal the word to the user when the game ends.



# secret_word = "travis"
# hangman(secret_word)

#
#
#
# # When you've completed your hangman function, scroll down to the bottom
# # of the file and uncomment the first two lines to test
# #(hint: you might want to pick your own
# # secret_word while you're doing your own testing)
#
#
# # -----------------------------------
#
#
#
# def match_with_gaps(my_word, other_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     other_word: string, regular English word
#     returns: boolean, True if all the actual letters of my_word match the
#         corresponding letters of other_word, or the letter is the special symbol
#         _ , and my_word and other_word are of the same length;
#         False otherwise:
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass
#
#
#
# def show_possible_matches(my_word):
#     '''
#     my_word: string with _ characters, current guess of secret word
#     returns: nothing, but should print out every word in wordlist that matches my_word
#              Keep in mind that in hangman when a letter is guessed, all the positions
#              at which that letter occurs in the secret word are revealed.
#              Therefore, the hidden letter(_ ) cannot be one of the letters in the word
#              that has already been revealed.
#
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass
#
#
#
# def hangman_with_hints(secret_word):
#     '''
#     secret_word: string, the secret word to guess.
#
#     Starts up an interactive game of Hangman.
#
#     * At the start of the game, let the user know how many
#       letters the secret_word contains and how many guesses s/he starts with.
#
#     * The user should start with 6 guesses
#
#     * Before each round, you should display to the user how many guesses
#       s/he has left and the letters that the user has not yet guessed.
#
#     * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
#
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#
#     * After each guess, you should display to the user the
#       partially guessed word so far.
#
#     * If the guess is the symbol *, print out all words in wordlist that
#       matches the current guessed word.
#
#     Follows the other limitations detailed in the problem write-up.
#     '''
#     # FILL IN YOUR CODE HERE AND DELETE "pass"
#     pass
#
#
#
# # When you've completed your hangman_with_hint function, comment the two similar
# # lines above that were used to run the hangman function, and then uncomment
# # these two lines and run this file to test!
# # Hint: You might want to pick your own secret_word while you're testing.
#
#
# if __name__ == "__main__":
#     # pass
#
#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
#
secret_word = choose_word(wordlist)
hangman(secret_word)
#
# ###############
#
#     # To test part 3 re-comment out the above lines and
#     # uncomment the following two lines.
#
    # secret_word = choose_word(wordlist)
#     #hangman_with_hints(secret_word)
