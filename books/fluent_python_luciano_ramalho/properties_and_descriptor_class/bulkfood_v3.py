# the descriptor is protocol-based, no inheritance is required to implement it
class Quantity:

    def __init__(self, storage_name):
        # in the each instance of `Quantity` is attribute `storage_name`: the name of the attribute that
        # stores the value of the managed instance
        self.storage_name = storage_name

    # the method `__set__`is called every time an attempt is made to assign a value to a managed attribute;
    # in this case `self` is an instance of the descriptor (`LineItem.weight` or `LineItem.price`),
    # `instance` is  a managed instance (instance of `LineItem`), `value` - assigned value
    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    # instances of the descriptor are associated with attributes
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
