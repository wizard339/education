import doctest

import model_v7 as model


class LineItem(model.Entity):
    """
    Tests:
        >>> raisins = LineItem('Golden raisins', 10, 6.95)
        >>> dir(raisins)[:3]
        ['_NonBlank#description', '_Quantity#price', '_Quantity#weight']
        >>> LineItem.description.storage_name
        '_NonBlank#description'
        >>> raisins.description
        'Golden raisins'
        >>> getattr(raisins, '_NonBlank#description')
        'Golden raisins'
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
