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

def lettersUsedAlready(userInput, letters_guessed):
    '''function that checks user input to see if it's in the list of already guessed letters'''
    if userInput in letters_guessed:
        return True
    else:
        return False

def unavilableLetters (letters_guessed):
    '''simple function that returns the letters guessed'''
    letters = " ".join(letters_guessed)
    return(letters)

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
        print(f"You have {(numGuesses - badLetters)} guesses remaining")


# The user starts with 3 warnings.
# 2. If the user inputs anything besides an alphabet (symbols, numbers), tell the
# user that they can only input an alphabet.
# a. If the user has one or more warning left, the user should lose one
# warning. Tell the user the number of remaining warnings.
# b. If the user has no remaining warnings, they should lose one guess.
# 3. If the user inputs a letter that has already been guessed, print a message
# telling the user the letter has already been guessed before.
# a. If the user has one or more warning left, the user should lose one
# warning. Tell the user the number of remaining warnings.
# b. If the user has no warnings, they should lose one guess.
# 4. If the user inputs a letter that hasn’t been guessed before and the letter is in
# the secret word, the user loses no​ guesses.
# 5. Consonants:​ If the user inputs a consonant that hasn’t been guessed and the
# consonant is not in the secret word, the user loses one​ guess if it’s a
# consonant.
# 6. Vowels:​ If the vowel hasn’t been guessed and the vowel is not in the secret
# ​​​​​​ word, the user loses two​ guesses. Vowels are a, e, i, o, and u. y does not
# count as a vowel.

def guessesRemainBool(letters_guessed,numGuesses,secret_word):
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

def checkSpecialCharacters(symbol):
    '''function to check a string for special characters'''
    specialCharacters = ("[@_!#$%^&*()<>?/\|}{~:] ")
    if symbol in specialCharacters:
        return True
    else:
        return False

def checkUserInput(userInput, letters_guessed):
    '''function to run through a list of validations to check the user input for incorrect values or format
    user input: should be a letter, if not this function confirms
    letters_guessed: list of letters previously guessed
    function should tell the user what they input incorrectly, if no error then it returns boolean of false
    '''
    if userInput.isnumeric():
        return("Oops! Please guess a letter not a number.")
    elif (checkSpecialCharacters(userInput) == True):
        return("Oops! That is not a letter, that's a symbol.")
    elif (len(userInput) > 1):
        return("Oops! You've input more than one character")
    elif (lettersUsedAlready(userInput, letters_guessed) == True):
        return("Oops! You've already guessed that letter before")
    else:
        return False

def warningSystem(userInput, numGuesses, letters_guessed):
    '''keeps track of warnings used'''
    warningCounter = 0
    warningsRemaining = 3
    if (userInput.isnumeric()) or (checkSpecialCharacters(userInput) == True) or (len(userInput) > 1) or (
            lettersUsedAlready(userInput, letters_guessed) == True):
        warningCounter += 1
        if warningCounter > 3:
            numGuesses -= 1
            return numGuesses
        elif warningCounter <= 3:
            warningsRemaining -= 1
            return warningsRemaining
    else:
        return warningsRemaining


def getLettersFromUser(letters_guessed,numGuesses):
    '''get letters from the user
    check to make sure the input is valid (ie. not a number and also only one letter at a time)'''

    lettersGuessedInput = ""
    while (is_word_guessed(secret_word, letters_guessed) == False) and (guessesRemainBool(letters_guessed, numGuesses, secret_word) == False):
        lettersGuessedInput = input("Please guess a letter: ")
        lettersGuessedInputLowercase = lettersGuessedInput.lower()
        for letter in lettersGuessedInput:
            if checkUserInput(lettersGuessedInput,letters_guessed) != False:
                # print(f"You have {warningSystem(lettersGuessedInput,numGuesses,letters_guessed)} warning's remaining.")
                print(checkUserInput(lettersGuessedInput,letters_guessed))
            else:
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
    warningsRemaining = 3
    letters_guessed = []
    print()
    print("Welcome to Hangman!")
    print()
    print(f"Your word {get_guessed_word(secret_word,letters_guessed)} has {len(secret_word)} characters, guess the letters correctly and you win.")
    print(f"You have {numGuesses} guesses, should you fail to guess the word, you'll hang!")
    print()
    get_guessed_word(secret_word, letters_guessed)

    while guessesRemainBool(letters_guessed,numGuesses,secret_word) == False:
        if is_word_guessed(secret_word,letters_guessed) == False:
            print("_____________________________________________________________")
            getLettersFromUser(letters_guessed, numGuesses)
            print()
            guessesRemaining(letters_guessed, numGuesses, secret_word)
            print(f"Choose from these letters: {get_available_letters(letters_guessed)}")
            print(f"You've guessed the following letters: {unavilableLetters(letters_guessed)}")
            print(get_guessed_word(secret_word, letters_guessed))
            print()
            print()
            print("_____________________________________________________________")
        elif is_word_guessed(secret_word, letters_guessed) == True:
            print()
            print()
            print()
            print("You've won!!!")
            print()
            print()
            print()
            break

# If the player runs out of guesses before completing the word, tell them they
# lost and reveal the word to the user when the game ends.

#4. The total score is the number of guesses_remaining once the user has
# guessed the secret_word times the number of unique letters in secret_word.

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

