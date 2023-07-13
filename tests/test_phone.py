import pytest

from src.item import Item
from src.phone import Phone


def test_phone_add():
    phone_1 = Phone('iPhone', 1000, 1, 2)
    phone_2 = Phone('Samsung', 500, 2, 1)

    assert phone_1 + phone_2 == 3


def test_phone_add_error():
    phone_1 = Phone('iPhone', 1000, 1, 2)

    with pytest.raises(TypeError):
        phone_1 + 1


def test_phone_add_item():
    phone_1 = Phone('iPhone', 1000, 1, 2)
    item_1 = Item('Samsung', 500, 2)

    assert phone_1 + item_1 == 3
