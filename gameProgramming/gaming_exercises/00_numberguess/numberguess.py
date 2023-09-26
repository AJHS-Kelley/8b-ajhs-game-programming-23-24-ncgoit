# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number.
# What happens if the guess is wrong?
	# Tell them the guess is wrong.
	# Tell them the number of guesses left.
	# Tell them if too high / too low.
# What happens if the guess is right?
	# Tell them the guess is right
	# Award a point.
# What happens if the player runs out of guesses?
	# Tell player round has been lost.
	# Award point to CPU.
# Check to see if player or CPU has >= 3 points, if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerGuess = -1
playerScore = 0
cpuScore = 0
numGuesses = 0
playerName = ""
difficulty = ""
rangeMin= -1
rangeMax = -1
numAttempts = -1

print("""

		+=========================+
        |                         |
        |    Guess the Number     |
        |          by             |
        |        Nevaeh C.        |
        |         2023            |
        +=========================+
    """)

playerName = input("What should I call you?\nType your name and press enter.\n")
#VERIFY INPUT WHENEVER POSSIBLE!
print(f"You want me to call you {playerName}. Is that correct?")
isCorrect = input("Please type Yes if correct, no if not correct.\n")
if isCorrect == "Yes":
	print(f"Ok {playerName}, let's continue!")
else:
    playerName = input("What should I call you?\nType your name and press enter.\n")
    
    
# CPU SECRET NUMBER GENERATION0 
secretNumber = random.randint(0,20)
print(secretNumber)

# PLAYER GUESS
print("You need to guess a number from 0 to 20 and you have four guesses.\n")

while playerScore != 3 or cpuScore != 3:
	# pass Tells Python to skip this block without giving an error.
    secretNumber = random.randint(0,20) # INCLUSIVE
    #print(secretNumber)
    playerGuess = int(input("Think of your number, type it in and then push ENTER"))
    # int() converts whatever is input into an INTERGER
    print(f"You have picked {playerGuess}. Let's see if it is a match!\n")
    for guesses in range(4):
        print(f"You have {4 - numGuesses} guesses left this round!\n")
        playerGuess = int(input("Think of your number, type it in and then push ENTER.\n"))
        # int () converts whatever is input into an INTEGER
        print(f"You have picked{playerGuess}. Let's see if it is a match!\n")
    if playerGuess == secretNumber:
        playerScore += 1
        print("A winner is you! It's a match!\n")
        break # immediately exit a loop!
    else:
        if playerGuess < secretNumber:
            print("Your guess is too low!\n")
        else:
            print("Your guess is too high!\n")
    numGuesses += 1
if playerGuess != secretNumber:
    cpuScore += 1
    print("You have won three rounds, so you win the game!\n")
else:
    print("Git gud scrub,  the CPU was able to smash you!\n")
    
