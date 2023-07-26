import csv
import os.path

from src.instantiate_csv_error import InstantiateCSVError



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name, self.price, self.quantity}"


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            self.__name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @classmethod
    def instantiate_from_csv(cls,path="../src/items.csv"):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Файл {path.split('/')[-1]} не найден")
            cls.all.clear()
            with open(path, "r", encoding="windows-1251") as file:
                file_reader = csv.DictReader(file)
                for row in file_reader:
                    if set(row)!= {"name","price","quantity"}:
                        raise InstantiateCSVError(path)
                    cls(row["name"], cls.string_to_number(row["price"]), cls.string_to_number(row["quantity"]))
        except (FileNotFoundError, InstantiateCSVError) as e:
            raise e




