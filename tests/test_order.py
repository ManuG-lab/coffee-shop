import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Customer.all_customers.clear()
    Coffee.all_coffees.clear()
    Order.all_orders.clear()

def test_valid_order():
    c = Customer("Lucy")
    coffee = Coffee("Americano")
    o = Order(c, coffee, 5.0)

    assert o.customer == c
    assert o.coffee == coffee
    assert o.price == 5.0

def test_invalid_customer():
    coffee = Coffee("Cappuccino")
    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 3.0)

def test_invalid_coffee():
    c = Customer("Mike")
    with pytest.raises(TypeError):
        Order(c, "NotCoffee", 3.0)

def test_invalid_price():
    c = Customer("Lena")
    coffee = Coffee("Latte")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)
    with pytest.raises(ValueError):
        Order(c, coffee, 12.0)
    with pytest.raises(ValueError):
        Order(c, coffee, "free")
