class Item:
    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

# Example of using the Item class
i = Item(10, 20)
print(f"Price: {i.price}, Weight: {i.weight}")
