"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
import csv


@pytest.fixture
def item():
    item1 = Item("Смартфон", 10000, 20)
    return item1


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000

@pytest.fixture
def item1():
    return Item(name="Widget", price=10.0, quantity=3)

def test_str(item1):
    assert str(item1) == "Widget"

def test_repr(item1):
    assert repr(item1) == "Item('Widget', 10.0, 3)"

@pytest.fixture
def csv_path():
    return '../src/items.csv'

def test_instantiate_from_csv(csv_path):
    Item.instantiate_from_csv(csv_path)
    with open(csv_path, 'r', encoding="windows-1251") as file:
        file_reader = csv.DictReader(file)
        for row in file_reader:
            item = Item(row['name'], int(float(row['price'])), int(float(row['quantity'])))
            assert item in Item.all




