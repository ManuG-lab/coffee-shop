# ☕ Coffee Shop Domain Modeling (Python OOP Project)

This project models a simple **Coffee Shop domain** using Python's Object-Oriented Programming principles. It defines core entities: Customer, Coffee, and Order, and establishes the relationships and business logic between them.

## 🚀 Features

- Create and manage Customer, Coffee, and Order objects.
- Enforce validation on attributes (name lengths, price range, types).
- Many-to-many relationships via orders.
- Aggregated statistics (number of orders, average price).
- Class method to find the top-spending customer for a specific coffee.

## 🧱 Project Structure

coffee_shop/
├── customer.py # Defines the Customer class
├── coffee.py # Defines the Coffee class
├── order.py # Defines the Order class
├── debug.py # For manual testing and debugging
├── tests/
│ ├── test_customer.py
│ ├── test_coffee.py
│ └── test_order.py
└── README.md 


## 🧪 Testing

Tests are written using pytest.

### Setup

pipenv install
pipenv shell
pipenv install pytest

Run Tests using - pytest
