"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone

item1 = Item("Смартфон", 10000, 20)
item3 = Item("питон", 10000, 20)
item4 = Phone("питон", 10000, 20, 2)

def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000

def test_apply_discount():
    Item.pay_rate = 0.8
    assert  Item.apply_discount(item1) == 8000

def test_string_to_number():
    assert  Item.string_to_number("5.5") == 5

def test_instantiate_from_csv():
    Item.instantiate_from_csv('file_test.csv')
    item2 = Item.all[0]
    assert item2.name == 'Смартфон'

def test_repr():
    assert repr(item3) == "Item('питон', '10000', 20)"

def test_str():
    assert str(item3) == "питон"

def test_phonerepr():
    assert repr(item4) == "Item('питон', 10000, 20, 2)"

def test_phonestr():
    assert str(item4) == "питон"

