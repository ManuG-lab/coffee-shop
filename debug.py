from customer import Customer
from coffee import Coffee
from order import Order

# Sample test
cust1 = Customer("Alice")
cust2 = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

cust1.create_order(latte, 4.5)
cust1.create_order(latte, 5.0)
cust2.create_order(latte, 6.0)
cust2.create_order(espresso, 3.5)

print(latte.average_price())
print(Customer.most_aficionado(latte).name)  # Should print Bob
