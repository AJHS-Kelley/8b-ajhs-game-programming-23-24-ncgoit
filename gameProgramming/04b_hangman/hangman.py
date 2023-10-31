# Hangman Game by Nevaeh Copeland, v0.4
import random
words = 'game four five dark moon read eating camera button avenue emerge demand raining absolute mountain sentence children changes trumpet delivery repeated abbreviation television theatre living contemplating jeopardizing naivenesses confused supercalifragilisticexpialidocious'.split()

# VARIABLE_NAMES in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
    =======''', '''
    +---+
    O   |
        |
        |
    =======''', '''
    +---+
    O   |
    |   |
        |
    =======''', '''
    +---+
    O   |
   /|   |
        |
    =======''', '''
    +---+
    O   |
   /|\  |
        |
    =======''', '''
    +---+
    O   |
   /|\  |
   /    |
    =======''', '''
    +---+
    O   |
   /|\  |
   / \  |
    =======''']

# Pick Word from list
def getRandomWord(wordList): # Return a random word from the list
    wordIndex = random.randint(0, len(wordList) - 1)
    # len(listName) -1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard (missedLetters, correctLetters, secreatWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()

    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
        print()

# i = 0
# while i < 50:
#     word = getRandomWord(words)
#     print(word)
#     i += 1


