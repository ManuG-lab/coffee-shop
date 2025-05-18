from order import Order

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        spenders = {customer: 0 for customer in cls.all_customers}
        for order in Order.all_orders:
            if order.coffee == coffee:
                spenders[order.customer] += order.price

        most = max(spenders.items(), key=lambda item: item[1], default=(None, 0))
        return most[0] if most[1] > 0 else None
