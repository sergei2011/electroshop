import csv


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
        super().__init__()
        #Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price*self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate
        return self.price

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def set_name(self, name):
        self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, path_items):
        cls.all = []
        with open(path_items) as f:
            file = csv.DictReader(f)
            for i in file:
                name = i['name']
                price = float(i['price'])
                quantity = int(i['quantity'])
                item = cls(None, None, None)
                item.name = name
                item.price = price
                item.quantity = quantity

                #list_techn = cls(name, price, quantity)
                #item.append(list_techn)
                cls.all.append(item)
            #print(cls.all[3])


    @staticmethod
    def string_to_number(str):
        return int(float(str))


    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity





