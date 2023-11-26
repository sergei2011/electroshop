from src.item import Item


class Phone(Item):
    def __init__(self, get_name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(get_name, price, quantity)
        self.number_of_sim = number_of_sim
    def __repr__(self):
        return f"Phone('{self.get_name}', {self.price}, {self.quantity}, {self.number_of_sim})"
    def __str__(self):
        return f'{self.get_name}'





