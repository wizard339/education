def quantity(storage_name):
    """
    property factory
    """
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def main():
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    assert nutmeg.weight == 8
    assert nutmeg.price == 13.95
    assert sorted(vars(nutmeg).items()) == [('description', 'Moluccan nutmeg'),
                                            ('price', 13.95), ('weight', 8)]


if __name__ == '__main__':
    main()
