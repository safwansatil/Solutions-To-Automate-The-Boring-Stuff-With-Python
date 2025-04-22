def displayInventory(inventory):
    print('Inventory items: ')
    itemTotal = 0
    for k,v in inventory.items():
        print(f"{k}: {v}")
        itemTotal+=v
    print(f"Total items: {itemTotal}")
    
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
            
inventory = {'coin': 42, 'sword':7, 'shield':3}
displayInventory(inventory)
dragonLoot = ['gold', 'skin', 'gold', 'sword']
addToInventory(inventory, dragonLoot)
print('After loot: ')
displayInventory(inventory)