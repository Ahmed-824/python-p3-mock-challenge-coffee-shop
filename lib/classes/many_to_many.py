class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Coffee name must be a string longer than 2 characters")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders

    def customers(self):
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0
        return sum(order.price for order in self._orders) / len(self._orders)

class Customer:
    def __init__(self, name):
        # Name validation and setter
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")
        self._name = value

    def orders(self):
        """Return all orders of the customer."""
        return self._orders

    def create_order(self, coffee, price):
        """Create a new order for the customer."""
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def coffees(self):
        """Return a list of unique coffees ordered by the customer."""
        return list(set(order.coffee for order in self._orders))

    @staticmethod
    def most_aficionado(coffee):
        """Return the customer who has spent the most on a given coffee."""
        orders = [order for order in coffee.orders if order.coffee == coffee]
        return max(orders, key=lambda o: o.price).customer if orders else None


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        customer._orders.append(self)
        coffee._orders.append(self)
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price