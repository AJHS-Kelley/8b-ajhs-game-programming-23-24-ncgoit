playerInventory = []
while len(playerInventory) < 10:
    playerInventory.append(input("Add an item to your inventory.\n"))
playerInventory.sort()
print(playerInventory)

while len(playerInventory) > 5:
   playerInventory.remove(input("You can now remove up to five items from your inventory.\n").lower())
playerInventory.sort()
print (playerInventory)
