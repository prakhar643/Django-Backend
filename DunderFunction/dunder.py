class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} and price is {self.price}"
    
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price


p1 = Product("Amul", 55)
p2 = Product("MotherDairy", 65)


print(p1)        # uses __str__
print(repr(p1))  # uses __repr__
print(p1 == p2)  # False
print(p1 < p2)   # True ✅