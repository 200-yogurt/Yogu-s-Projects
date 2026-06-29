from utils import *

class Character:

    def __init__(self,
                 name,
                 health=100,
                 damage=10,
                 ):
        
        self.name = name
        self.health = health
        self.damage = damage

    def display_stats__(self):

        print(f"// {self.name} //")
        print(f"HP:  {self.health}")
        print(f"DMG:  {self.damage}")
        print()

    def attack__(self, foe):

        narrate__(f"\n== {self.name} ATTACKED! == ", fast)

        dmg = self.damage
        foe.health -= dmg

        narrate__(f"\n== Dealt:  {dmg} Damage! ==\n", moderate)