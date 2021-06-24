""" evaluating object oriented programming in python """


class Shirt:
    """Testing with a shirt object"""

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        """Initialize the shirt attributes"""
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        """change the shirt price"""
        self.price = new_price

    def discount(self, discount):
        """apply the shirt discount"""
        return self.price * (1 - discount)


Shirt("red", "S", "short sleeve", 15)

new_shirt = Shirt("red", "S", "short sleeve", 15)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

new_shirt.change_price(10)
print(new_shirt.price)

print(new_shirt.discount(0.2))

tshirt_collection = []
shirt_one = Shirt("orange", "M", "short sleeve", 25)  # shirt instantiations are object references
shirt_two = Shirt("red", "S", "short sleeve", 15)
shirt_three = Shirt("purple", "XL", "short sleeve", 10)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

# RFX: change this to enumerate
for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)
