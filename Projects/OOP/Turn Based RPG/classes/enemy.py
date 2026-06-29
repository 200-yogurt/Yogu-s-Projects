from classes.character import Character

class Enemy(Character):

    def __init__(self, name, health=100, damage=10):

        super().__init__(name, health, damage)
