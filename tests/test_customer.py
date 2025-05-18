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

def test_valid_customer_name():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_invalid_customer_name():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLong")

def test_customer_orders_and_coffees():
    c = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")

    c.create_order(coffee1, 3.5)
    c.create_order(coffee2, 4.0)

    assert len(c.orders()) == 2
    assert coffee1 in c.coffees()
    assert coffee2 in c.coffees()

def test_most_aficionado():
    c1 = Customer("Alice")
    c2 = Customer("Bob")
    coffee = Coffee("Espresso")

    c1.create_order(coffee, 4.0)
    c1.create_order(coffee, 2.0)
    c2.create_order(coffee, 9.0)

    assert Customer.most_aficionado(coffee) == c2
