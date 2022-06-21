import doctest

import model_v4c as model

class LineItem:
    """
    Tests:
        >>> from bulkfood_v4c import LineItem
        >>> coconuts = LineItem('Brazilian coconut', 20, 17.95)
        >>> coconuts.weight, coconuts.price
        (20, 17.95)
    """
    
    # now don't need to pass the name of the managed attribute
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
