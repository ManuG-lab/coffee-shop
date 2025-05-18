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

def test_valid_coffee_name():
    c = Coffee("Latte")
    assert c.name == "Latte"

def test_invalid_coffee_name():
    with pytest.raises(ValueError):
        Coffee("A")

def test_coffee_orders_and_customers():
    coffee = Coffee("Mocha")
    c1 = Customer("John")
    c2 = Customer("Jane")

    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()

def test_num_orders_and_avg_price():
    coffee = Coffee("Flat White")
    customer = Customer("Sam")

    customer.create_order(coffee, 2.0)
    customer.create_order(coffee, 4.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 3.0
