from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
        raise TypeError("нельзя  сложить Phone или Item с экземплярами не Phone или Item классов")

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity, self.number_of_sim}"
