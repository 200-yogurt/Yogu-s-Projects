from classes.player import Player

yogu = Player("Yogu")

print(yogu)
print(yogu.inventory)

yogu.increase_damage__(5)
yogu.hurt__(6.22)

print(yogu)

yogu.inventory.add_item__("Sword")
yogu.inventory.add_item__("Sword", 4)
yogu.inventory.add_item__("Potion", 2)
yogu.inventory.remove_item__("Potion")
yogu.inventory.remove_item__("Bow")
yogu.inventory.remove_item__("Sword", 5)
yogu.inventory.add_item__("Sword", 2)
yogu.inventory.add_item__("Shurikens", 15)
yogu.inventory.add_item__("Staff")
print(yogu.inventory)
yogu.inventory.clear__()

print(yogu.inventory)