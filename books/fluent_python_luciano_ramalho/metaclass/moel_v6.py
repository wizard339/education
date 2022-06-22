import abc


class AutoStorage:
    """a descriptor class that automatically manages attributes of storage"""
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):
    """an abstract subclass AutoStorage that overrides the __set__ method calling the `validate` abstract method"""
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """returns a verified value and raises ValueError"""


class Quantity(Validated):
    """number is better zero"""
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return


class NonBlank(Validated):
    """the string contains at least one space"""
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value can not be empty or blank')
        return value


def entity(cls):
    """a class decorator designed to form a class name as like `_<descriptor_class>#<managed_attribute>`"""
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = '_{}#{}'.format(type_name, key)
    return cls
