import abc

class Tombola(abc.ABC):
    
    @abc.abstractmethod
    
    def load(self, iterable):
        """Добавить элементы из итерируемого объекта."""
        
    @abc.abstractmethod
    
    def pick(self):
        """Извлечь случайный элемент и вернуть его.
        
        Этот метод должен возбуждать исключение `LookupError`,
        если объект пуст.
        """
        
    def loaded(self):
        """Вернуть `True`, если хотя бы 1 элемент, иначе `False`."""
        return bool(self.inspect())
        
    def inspect(self):
        """Вернуть отсортированный кортеж, содержащий находящиеся в
        контейнере элементы.
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
