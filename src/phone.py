from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim
    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        self.quantity + other.quantity

phone1 = Phone("iPhone 14", 120_000, 5, 2)
print(repr(phone1))

