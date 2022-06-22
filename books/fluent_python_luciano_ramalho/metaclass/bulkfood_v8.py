import doctest

import model_v8 as model


class LineItem(model.Entity):
    """
    Tests:
        >>> for name in LineItem.field_names():
        ...     print(name)
        ...
        description
        weight
        price
    """
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    doctest.testmod(verbose=True)
