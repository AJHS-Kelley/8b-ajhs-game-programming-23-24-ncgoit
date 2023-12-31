# Collections Examples, Nevaeh Copeland, v0.5a
# List -- ORDEED, CHANGEABLE, ALLOWS DUPLICATE VALUES
# breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk"]
# Each item on the list is known as an ELEMENT.
# The position in the list for each is the INDEX.
# The element "BACON" is at index 0.
# Python Only: index -1 it is the last item on the list.
# testScores = [95, 100, 25, 15, 27, 35]
# classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

#Printing Contents of an List
#print(breakfastFoods)
#print(testScores)
#print(classGPA)

#Accessing Specific List Elements -- REMEMBER THE FIRST ELEMENT IS INDEX 0
#print(breakfastFoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastFoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

# Pause - WYOC -- Acces the third Element in Each List
# print(breakfastFoods[2])
# print(testScores[2])
# print(classGPA[2])

# Changing Items in a List
# breakfastFoods[0] = "Sausage"
# testScores[0] = 97
# classGPA[0] = 3.75 
# print(breakfastFoods[0])
# print(testScores[0])
# print(classGPA[0])
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# Pause -- WYOC -- Change 5th Element
# breakfastFoods[4] = "Eggs"
# testScores[4] = 86
# classGPA[4] = 2.21
# print(breakfastFoods)
# print(testScores)
# print(classGPA)

# Adding and Inserting Items to a List
# .append() adds an item to the END of a list.
# breakfastFoods.append("hash browns")
# print(breakfastFoods)
# testScores.append(99)
# print(testScores)
# classGPA.append(1.99)
# print(classGPA)

#.insert() allows you to place an item at a specific index in the list.
# breakfastFoods.insert(3, "Parfait")
# print(breakfastFoods)
# testScores.insert(3, 55)
# print(testScores)
# classGPA.insert(3, 0.0)
# print(classGPA)

# Pause -- WYOC .append() another item to each list. .insert() an item at index 5.
# breakfastFoods.append("toast")
# print(breakfastFoods)
# testScores.append(74)
# print(testScores)
# classGPA.append(3.75)
# print(classGPA)

# breakfastFoods.insert(5, "grits")
# print(breakfastFoods)
# testScores.insert(5, 67)
# print(testScores)
# classGPA.insert(5, 3.21)
# print(classGPA)

# Deleting Items from a list
# Use .remove() to remove a specific item from the list
# breakfastFoods.remove("Waffles")
# print(breakfastFoods)
# testScores.remove(100)
# print(testScores)
# classGPA.remove(2.25)
# print(classGPA)

# To delete using the index value we use .pop()
# breakfastFoods.pop(4)
# print(breakfastFoods)
# testScores.pop(4)
# print(testScores)
# classGPA.pop(4)
# print(classGPA)

# PAUSE - WYOC -- .pop() the 2nd element from each list. .remove() any item from the list.
# breakfastFoods.pop(1)
# print(breakfastFoods)
# testScores.pop(1)
# print(testScores)
# classGPA.pop(1)
# print(classGPA)

# breakfastFoods.remove("Cereal")
# print(breakfastFoods)
# testScores.remove(95)
# print(testScores)
# classGPA.remove(3.14)
# print(classGPA)

# Determining List Length
# print(f"There are {len(breakfastFoods)} items in the breakfastFoods list.")
# print(f"There are {len(testScores)} items in the testScores list.")
# print(f"There are {len(classGPA)} items in the classGPA")

# List Methods -- Functions for working with lists.
# Sorting Lists -- Alphanumerical -- Ascending -- Captial Letters before Lower Case Letters
# print(f"The original breakfastFoods list is {breakfastFoods}.")
# breakfastFoods.sort()
# print(f"The sorted breakfastFoods list is {breakfastFoods}.")
# print(f"The original testScores list is {testScores}.")
# testScores.sort()
# print(f"The sorted testScores list is {testScores}.")
# print(f"The original classGPA list is {classGPA}.")
# classGPA.sort()
# print(f"The sorted classGPA list is {classGPA}.")

breakfastFoods = ["Bacon", "Waffles", "Pancakes", "Cereal", "Milk", "Bacon"]
testScores = [95, 100, 25, 15, 27, 35, 25]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25, 2.25]

# .count() will return the number of times a value appears in a list.
# numWaffles = breakfastFoods.count("Waffles")
# print(f"There are {numWaffles} Wafefles in the list.")
# numBacon = breakfastFoods.count("Bacon")
# print(f"There are {numBacon} Bacon in the list.")
# Pause -- WYOC -- Use .count() to count for a single item in the list and multiple items. Use testScores and classGPA.
# testCount = testScores.count(95)
# print(f"The number 95 was scored {testCount} times.")
# testCount = testScores.count(25)
# print(f"The number 25 was scored {testCount} times.")
# gpaCount = classGPA.count(3.14)
# print(f"There is {gpaCount} GPA lower 1.0 ")
# gpaCountRepeat = classGPA.count(2.25)
# print(f"There is {gpaCountRepeat} GPA equal to 2.25")

# Delete All Contents of a List -- .clear()
# breakfastFoods.clear()
# print(f"The breakfast foods list is {breakfastFoods}")
# testScores.clear()
# print(f"The test scores list is {testScores}")
# classGPA.clear()
# print(f"The class gpa list is {classGPA}")

# Common Bugs -- Index Out of Range
print(f"The last item in the list is {breakfastFoods[5]}.")

print(f"The last item in the testScores list is {testScores[len(testScores) - 1]}")
