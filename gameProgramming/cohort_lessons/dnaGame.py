# DNA Replication Game, Ryan Kelly, v0.1

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

dna = genDNA()

def genRNA(dnaSquence: str) -> tuple:
    print(f"The DNA Sequence is a {dnaSquence}.\n")
    print("You willnow generate the RNA sequence that would match.\n")
    print("Please Remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart= time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan. 01, 1776
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return(rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can reference elements with the index.
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

rna = genRNA(dna)
print(rna)