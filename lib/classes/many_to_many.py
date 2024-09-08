class Coffee:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) <= 2:
            raise ValueError("Coffee name must be a string longer than 2 characters.")
        self._name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value != self._name:
            raise AttributeError("Cannot change the name of the coffee")
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise ValueError("Order must be of type Order.")
        self._orders.append(order)
    
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
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = name
        self._orders = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value != self._name:
            raise AttributeError("Name is immutable")
    
    def add_order(self, order):
        if not isinstance(order, Order):
            raise ValueError("Order must be of type Order.")
        self._orders.append(order)
    
    def orders(self):
        return self._orders
    
    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be of type Coffee.")
        order = Order(self, coffee, price)
        return order

class Order:
    all_orders = []
    
    def __init__(self, customer, coffee, price):
        if not isinstance(price, (float, int)) or price <= 0:
            raise ValueError("Price must be a positive number.")
        
        self._price = price
        self.customer = customer
        self.coffee = coffee
        customer.add_order(self)
        coffee.add_order(self)
        Order.all_orders.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value != self._price:
            raise AttributeError("Price cannot be changed")
    
    @classmethod
    def all(cls):
        return cls.all_orders