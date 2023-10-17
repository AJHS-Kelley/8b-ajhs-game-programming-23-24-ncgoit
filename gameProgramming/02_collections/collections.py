# playerInventory = []
# while len(playerInventory) < 10:
#     playerInventory.append(input("Add an item to your inventory.\n"))
# playerInventory.sort()
# print(playerInventory)

# while len(playerInventory) > 5:
#    playerInventory.remove(input("You can now remove up to five items from your inventory.\n").lower())
# playerInventory.sort()
# print (playerInventory)

# doorKeys = [
#     "red",
#     "blue",
#     "green",
#     "purple",
#     "pink"
# ]
# key = input("Which color key do you need to unlock the door?\n")
# if key in doorKeys:
#     print("You have the correct key! The door unlocks.\n")
# else:
#     print("You do not have that key. The door remains locked.\n")

weaponList = [
    True, # Machette
    False, # Sword
    False, # Boot
    False, # army of ants
    True, # C4
    False, # Nukes
    True # Gun
]

weaponNum = 0
while weaponNum < len(weaponList):
    if weaponNum == 0 and weaponList [0] == True:
        print("You are wielding a sharp machette.\n")
    if weaponNum == 1 and weaponList [0] == True:
        print("You are wielding a shiny sword.\n")
    if weaponNum == 2 and weaponList [0] == True:
        print("You are wielding a flumsy boot.\n")
    if weaponNum == 3 and weaponList [0] == True:
        print("You are wielding a controller that controls ants.\n")
    if weaponNum == 4 and weaponList [0] == True:
        print("You are wielding a c4 explosive.\n")
    if weaponNum == 5 and weaponList [0] == True:
        print("You are wielding a nuclear bomb.\n")
    if weaponNum == 6 and weaponList [0] == True:
        print("You are wielding a AK47.\n")
