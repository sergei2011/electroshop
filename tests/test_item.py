"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)

def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000

def test_apply_discount():
    Item.pay_rate = 0.8
    assert  Item.apply_discount(item1) == 8000
