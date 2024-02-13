# Object-Oriented Programming, Nevaeh Copeland, v0.3

class Person: # Use PascalCase for ClassNames
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None

        # TO String Function -- How the object appears as a string.
    def __str__(self):
        return f"Name: {self.name}\nThis Person is {self.age} years old. \nThey weigh {self.weight} pounds."
    def classFunction(self):
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")



person1 = Person("DoodleBob", 1, 0.0625)
person2 = Person("Scooby Doo",7 ,150)
# print(person1)
# print(person2)

# if person1.weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#     print("Each person weighs the same.")
# else:
#     print(f"{person2.name} weighs more than {person1.name}.")

# # WYOC --

# if person1.age > person2.age:
#     print(f"{person1.name} is older than {person2.name}.")
# elif person1.age == person2.age:
#     print("They are the same age.")
# else:
#     print(f"{person2.name} is older than than {person1.name}.")

# person1.classFunction()

# Changing Properties After Creation
print(person1.name)
person1.name = "Madalorian"
print(person1.name)

# Deleting Properties -- DANGER ROBINSON, DANGER!
# THIS IS NOT 'RESET' A PROPERTY, IT DELETES IT COMPLETELY
print(person1.weight)
del(person1.weight)
# print(person1.weight)

# Deleting Objects -- Delete them if you're finished with them.
del person1

# Adding Properties to Objects
person2.weakness = "Taking an L"
print(person2)
print(person2.weakness)