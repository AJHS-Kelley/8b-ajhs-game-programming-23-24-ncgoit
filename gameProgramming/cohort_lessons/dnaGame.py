# DNA Replication Game, Ryan Kelly, v0.0

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
print(dna)