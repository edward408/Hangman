 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    t=0
    if lettersGuessed ==[]:
        return False
    for i in lettersGuessed:
        if i in secretWord:
            t+=1
    if t == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guesses =''
    for i in secretWord:
        if i in lettersGuessed:
            guesses+=i
        else:
            guesses+=' _ '

    return guesses



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lets = string.ascii_lowercase
    for letter in lets:
        if letter in lettersGuessed:
            lets = lets.replace(letter, "")

    return lets

  

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    mistakesMade=0
    chances =8
    available = getAvailableLetters(lettersGuessed)
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is"+" "+ str(len(secretWord))+" "+"letters long"
    print " ---------------"
    while mistakesMade <8:
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
        
        else:
            
            print "You have " + str(chances) + " " + "guesses left"
            print "Available letters:" + "" + getAvailableLetters(lettersGuessed)
            guess = raw_input("Please enter a letter: ").lower()
            if len(guess) >1:
                print "Error! Only 1 character is allowed!
                sys.exit()
                
            elif guess in secretWord:
                lettersGuessed.append(guess)
                getword = getGuessedWord(secretWord,lettersGuessed)
                print "Good guess:" + getword
                print "---------------"
            elif guess not in secretWord:
                mistakesMade+=1
                chances -=1
                getword =getGuessedWord(secretWord, lettersGuessed)
                print "Oops! That letter is not in my word" +""+(getword)
                print "---------------"
                if mistakesMade == 8:
                    print"Sorry, you ran out of guesses. The word was" +" "+secretWord





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'listo'
# secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
