# Hangman Game by Nevaeh Copeland, v0.2

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

i = 0
while i < len(HANGMAN_BOARD):
    print(HANGMAN_BOARD[i])
    i += 1
