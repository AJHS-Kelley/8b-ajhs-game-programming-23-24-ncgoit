# Data Types and Operators, Nevaeh Copeland, v0.7

# Variable Rules
# CANNOT START WITH A NUMBER !!!!!
# CANNOT USE BUILT-IN KEYWORDS AS VARIABLES.
# VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED.
# snake_case variables use _ to seperate words, all lower case.
# camelCase variables do not use spaces, 1st word lower, rest upper.

# String Literal Examples
playerName = "John Doe"
emptyString = ""
spaceString = " "
playerUsername = "Bones"

# Interger Data Types
health = 100
extraLives = 5
temperature = -17

# Floating Point data Types
pi =3.1415678
lapTime = 3.5
velocity = -2.0
mapSize = 4.567

# Boolean Data Types
isFireType = False
weaponEquipped = True
pvpEnabled = False
mulitplayerOn = False

# Aritmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(5 + -2) #Addition
print(17 - 2) #Subtraction
print(2 * 3)  # Mulitiplication
print(-8 / 4) # Division
print(9 ** 3) # Exponents
print(16 % 2) #m Modules -- Divides, then returns remainder, most commonly used to determine even/odd

# Comparison Operators
# Evaluate the expression then return True or False
print(6 > 3)  # Greater Than
print(8 >= -3) # Greater Than or Equal to
print(-8 < -10) # Less Than
print(14 == 8)  # Is Equal To
print(-21 != 12)  # Not Equal To

# Assignment Operators
myVariable = "myValue" # Give variable on the left value on the right, throw out any curerent value
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logic Operators
print(3 > 5) and (4 < 3) # AND requires ALL expressins to be True
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor = "Blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires ONE epression to be True.
print(5 > 2 or 2 < 5)
print(3 != 3 or 5 == 5)

# AND OR Combied
print("Line 81")
print(3 > 2 and 4 < 3 or 5 != 7)
# print(True and False or True)

# NOT Logical Operator
print(not (3 > 2) )
print(not (not (not (5 != 3))))
