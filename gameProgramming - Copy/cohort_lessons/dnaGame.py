# DNA Replication Game, Ryan Kelly, v0.1
# Code works as expected. 

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tol.
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a position intergar number of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence


def doTranscription(dnaSquence: str) -> tuple:
    print(f"The DNA Sequence is a {dnaSquence}.\n")
    print("You will now generate the RNA sequence that would match.\n")
    print("Please Remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart= time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1776
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return(rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are different lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
         if dnaBase == "A" and rnaBase == "U":
            isMatch = True
         elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
         elif dnaBase == "G" and rnaBase == "C":
            isMatch =True
         elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
         else:
            print ("Unable to identify correct base. No match detected.")
    return isMatch

def calcScore(rnaSequence: str, rnaTime):
    score = 0
    if rnaTime < 1.0:
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 700000
    elif rnaTime < 25.0:
        score += 500000
    else: # Slowest Time, Lowest Score
        score += 250000

    scoreMulti = 0.0
    if len(rnaSequence) >= 30: # Longest Sequence, Highest Mulitplier
        scoreMulti = 5.0
    elif len(rnaSequence) >= 25:
        scoreMulti = 4.0
    elif len(rnaSequence) >= 20:
        scoreMulti = 3.0
    elif len(rnaSequence) >= 15:
        scoreMulti = 2.0
    elif len(rnaSequence) >= 5:
        scoreMulti = 1.0
    else: # Shortest sequence, Lower Multiplier
        scoreMulti = 0.25
    # Increase Score, multiplier should be > 1.0
    # Decrease Score, multiplier should be < 1.0
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    #File Modes
    # "x" mode -- CREATE FILE, IF FILE EXIST, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXIST, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f" DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time:{rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()



dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1],score)

