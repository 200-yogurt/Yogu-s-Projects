class Inventory:

    def __init__(self):
    
        self.items = {}

    def __str__(self):
        
        return f"Inventory = {self.items}"


    def add_item__(self, item, amount=1):

        if item in self.items:

            self.items[item] += amount
            return

        self.items[item] = amount

    def remove_item__(self, item, amount=1):

        if item not in self.items:

            print("Item not found")
            return

        self.items[item] -= amount

        if self.items[item] <= 0:

            self.items.pop(item, None)

    def clear__(self):

        self.items.clear()