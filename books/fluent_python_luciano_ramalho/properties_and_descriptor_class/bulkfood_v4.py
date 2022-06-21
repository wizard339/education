import doctest


class Quantity:
    # this attribute is needed to count instances of `Quantity`
    __counter = 0
    
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    # we have to implement the method `__get__` because the name of the managed attribute
    # does not match the value `storage_name`
    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    """
    Tests:
        >>> from bulkfood_v4 import LineItem
        >>> coconuts = LineItem('Brazilian coconut', 20, 17.95)
        >>> coconuts.weight, coconutsversion .price
        (20, 17.95)
        >>> getattr(coconuts, '_Quantity#0'), getattr(coconuts, '_Quantity#1')
        (20, 17.95)
    """
    
    # now don't need to pass the name of the managed attribute
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    doctest.testmod(verbose=True)
