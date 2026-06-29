from classes.inventory import Inventory

class Player:
    
    def __init__(self,
                 name,
                 health=10,
                 damage=1):
        
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = Inventory()

    def __str__(self):
        
        return f" == Player Data ==\n\nName = {self.name}\nHealth = {self.health}\nDamage = {self.damage}\n"


    def heal__(self, amount):

        self.health += amount

    def hurt__(self, amount):

        self.health -= amount

    def increase_damage__(self, amount):

        self.damage += amount

    def change_name__(self, new_name):

        self.name = new_name