from classes.character import Character

class Player(Character):

    def __init__(self, name, health=100, damage=10):

        super().__init__(name, health, damage)
