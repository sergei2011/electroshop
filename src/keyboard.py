from src.item import Item


class Lang:
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language
    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"




class Keyboard(Item, Lang):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price,quantity)
        self.__language = language
        if self.__language.upper() != "EN" and self.__language.upper() != "RU":
            raise ValueError("AttributeError: property 'language' of 'Keyboard' object has no setter")

kb = Keyboard('Dark Project KD87A', 9600, 5)
kb.language = 'CH'
#kb.change_lang()
print(kb.language)